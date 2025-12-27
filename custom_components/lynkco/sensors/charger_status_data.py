from .lynk_co_sensor import LynkCoSensor


# Dutch translations for charger statuses
CHARGER_CONNECTION_STATUS = {
    "CHARGER_CONNECTION_UNSPECIFIED": "Onbekend",
    "CHARGER_CONNECTION_DISCONNECTED": "Losgekoppeld",
    "CHARGER_CONNECTION_CONNECTED_WITHOUT_POWER": "Verbonden (geen stroom)",
    "CHARGER_CONNECTION_POWER_AVAILABLE_BUT_NOT_ACTIVATED": "Stroom niet geactiveerd",
    "CHARGER_CONNECTION_CONNECTED_WITH_POWER": "Verbonden",
    "CHARGER_CONNECTION_INIT": "Initialiseren",
    "CHARGER_CONNECTION_FAULT": "Storing",
}

CHARGER_STATE = {
    "CHARGER_STATE_UNSPECIFIED": "Onbekend",
    "CHARGER_STATE_IDLE": "Inactief",
    "CHARGER_STATE_PRE_STRT": "Voorbereiden",
    "CHARGER_STATE_CHARGN": "Laden",
    "CHARGER_STATE_ALRM": "Alarm",
    "CHARGER_STATE_SRV": "Service",
    "CHARGER_STATE_DIAG": "Diagnose",
    "CHARGER_STATE_BOOT": "Opstarten",
    "CHARGER_STATE_RSTRT": "Herstarten",
}


def create_sensors(coordinator, vin):
    sensors = [
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Charger connection status",
            "vehicle_shadow.evs.chargerStatusData.chargerConnectionStatus",
            state_mapping=CHARGER_CONNECTION_STATUS,
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Charger Updated",
            "vehicle_shadow.evs.chargerStatusData.updatedAt",
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Charge state",
            "vehicle_shadow.evs.chargerStatusData.chargerState",
            state_mapping=CHARGER_STATE,
        ),
    ]
    return sensors
