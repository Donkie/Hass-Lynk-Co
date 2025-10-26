import logging
import re

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.data_entry_flow import FlowResult
import aiohttp

from .const import (
    CONFIG_REDIRECT_URI_KEY,
    CONFIG_DARK_HOURS_END,
    CONFIG_DARK_HOURS_START,
    CONFIG_EXPERIMENTAL_KEY,
    CONFIG_SCAN_INTERVAL_KEY,
    CONFIG_VIN_KEY,
    DOMAIN,
    STORAGE_REFRESH_TOKEN_KEY,
)
from .login_flow import (
    get_auth_uri,
    get_tokens_from_redirect_uri,
)
from .token_manager import STORAGE_CCC_TOKEN_KEY, get_token_storage, send_device_login

_LOGGER = logging.getLogger(__name__)

STEP_USER_DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONFIG_REDIRECT_URI_KEY): str,
        vol.Required(CONFIG_VIN_KEY): str,
    }
)


def is_valid_vin(vin: str) -> bool:
    """Validate the VIN based on length and allowed characters."""
    vin_regex = r"^[A-HJ-NPR-Z0-9]{17}$"
    return bool(re.match(vin_regex, vin))


def is_valid_redirect_uri(redirect_uri: str) -> bool:
    """Basic validation for redirect URI format."""
    return redirect_uri.startswith("msauth://prod.lynkco.app.crisp.prod/")


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Lynk & Co."""

    VERSION = 1

    @staticmethod
    def async_get_options_flow(config_entry):
        """Return the options flow handler."""
        return OptionsFlowHandler(config_entry)

    async def async_step_user(self, user_input=None):
        """Handle a flow initialized by the user."""
        errors = {}

        session = aiohttp.ClientSession()
        self.context["session"] = session

        if user_input:
            redirect_uri = user_input.get(CONFIG_REDIRECT_URI_KEY)
            vin = user_input.get(CONFIG_VIN_KEY)

            if not redirect_uri or not vin:
                errors["missing_details"] = "missing_details"
            else:
                if not is_valid_vin(vin):
                    errors["vin"] = "invalid_vin"
                if not is_valid_redirect_uri(redirect_uri):
                    errors["redirect_uri"] = "invalid_redirect_uri"

            if not errors:
                access_token, refresh_token = await get_tokens_from_redirect_uri(
                    redirect_uri,
                    self.context.get("login_code_verifier"),
                    self.context.get("session"),
                )

                # Close the session
                await session.close()

                if access_token and refresh_token:
                    token_storage = get_token_storage(self.hass)
                    tokens = await token_storage.async_load() or {}
                    tokens[STORAGE_REFRESH_TOKEN_KEY] = refresh_token
                    ccc_token = await send_device_login(access_token)
                    if ccc_token:
                        tokens[STORAGE_CCC_TOKEN_KEY] = ccc_token
                    else:
                        _LOGGER.error("New ccc token is none")
                    await token_storage.async_save(tokens)
                    if hasattr(self, "_reauth_entry"):
                        # Update the existing config entry
                        self.hass.config_entries.async_update_entry(
                            self._reauth_entry,
                            data={"vin": vin},
                        )
                        await self.hass.config_entries.async_reload(
                            self._reauth_entry.entry_id
                        )
                        return self.async_abort(reason="reauth_successful")
                    else:
                        # Create new entry
                        return self.async_create_entry(
                            title="Lynk & Co",
                            data={"vin": vin},
                            description_placeholders={
                                "additional_configuration": "Please use the configuration to enable experimental features."
                            },
                        )
            else:
                # Re-show the form with errors if validation fails
                auth_url, code_verifier, code_challenge = get_auth_uri()
                self.context["login_code_verifier"] = code_verifier
                self.context["login_code_challenge"] = code_challenge

                return self.async_show_form(
                    step_id="user",
                    data_schema=STEP_USER_DATA_SCHEMA,
                    description_placeholders={"auth_url": auth_url},
                    errors=errors,
                )

        auth_url, code_verifier, code_challenge = get_auth_uri()
        self.context["login_code_verifier"] = code_verifier
        self.context["login_code_challenge"] = code_challenge

        return self.async_show_form(
            step_id="user",
            data_schema=STEP_USER_DATA_SCHEMA,
            description_placeholders={"auth_url": auth_url},
            errors=errors,
        )

    async def async_step_reauth(self, user_input=None):
        """Handle the re-authentication flow."""
        self._reauth_entry = self.hass.config_entries.async_get_entry(
            self.context["entry_id"]
        )

        if user_input is not None:
            return await self.async_step_user(user_input)

        auth_url, code_verifier, code_challenge = get_auth_uri()
        self.context["login_code_verifier"] = code_verifier
        self.context["login_code_challenge"] = code_challenge

        return self.async_show_form(
            step_id="user",
            data_schema=STEP_USER_DATA_SCHEMA,
            description_placeholders={"auth_url": auth_url},
            errors=errors,
        )


class OptionsFlowHandler(config_entries.OptionsFlow):
    def __init__(self, config_entry: config_entries.ConfigEntry) -> None:
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None) -> FlowResult:
        if user_input is not None:
            # Save the options and conclude the options flow
            return self.async_create_entry(title="", data=user_input)

        data_schema = vol.Schema(
            {
                vol.Required(
                    CONFIG_EXPERIMENTAL_KEY,
                    default=self.config_entry.options.get(
                        CONFIG_EXPERIMENTAL_KEY, False
                    ),
                ): bool,
                vol.Required(
                    CONFIG_SCAN_INTERVAL_KEY,
                    default=self.config_entry.options.get(
                        CONFIG_SCAN_INTERVAL_KEY, 120
                    ),
                ): vol.All(vol.Coerce(int), vol.Range(min=60, max=1440)),
                vol.Required(
                    CONFIG_DARK_HOURS_START,
                    default=self.config_entry.options.get(CONFIG_DARK_HOURS_START, 1),
                ): vol.All(vol.Coerce(int), vol.Range(min=0, max=23)),
                vol.Required(
                    CONFIG_DARK_HOURS_END,
                    default=self.config_entry.options.get(CONFIG_DARK_HOURS_END, 5),
                ): vol.All(vol.Coerce(int), vol.Range(min=0, max=23)),
            }
        )

        # Display or re-display the form with the current options as defaults
        return self.async_show_form(
            step_id="init",
            data_schema=data_schema,
        )
