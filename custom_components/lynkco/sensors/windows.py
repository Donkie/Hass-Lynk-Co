from .lynk_co_sensor import LynkCoSensor


# Dutch translations for window statuses
WINDOW_STATUS = {
    "WINDOW_STATUS_CLOSED": "Dicht",
    "WINDOW_STATUS_OPEN": "Open",
    "WINDOW_STATUS_AJAR": "Op een kier",
    "WINDOW_STATUS_UNSPECIFIED": "Onbekend",
    "WINDOW_CLOSED": "Dicht",
    "WINDOW_OPEN": "Open",
    "WINDOW_AJAR": "Op een kier",
    "CLOSED": "Dicht",
    "OPEN": "Open",
}

SUNROOF_STATUS = {
    "SUNROOF_OPEN_STATUS_CLOSED": "Dicht",
    "SUNROOF_OPEN_STATUS_OPEN": "Open",
    "SUNROOF_OPEN_STATUS_AJAR": "Op een kier",
    "SUNROOF_OPEN_STATUS_TILTED": "Gekanteld",
    "SUNROOF_OPEN_STATUS_UNSPECIFIED": "Onbekend",
    "SUNROOF_CLOSED": "Dicht",
    "SUNROOF_OPEN": "Open",
    "SUNROOF_AJAR": "Op een kier",
    "SUNROOF_TILTED": "Gekanteld",
    "CLOSED": "Dicht",
    "OPEN": "Open",
    "TILTED": "Gekanteld",
}


def create_sensors(coordinator, vin):
    sensors = [
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Window Status Driver",
            "vehicle_shadow.vls.windowStatusDriver",
            state_mapping=WINDOW_STATUS,
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Window Status Driver Rear",
            "vehicle_shadow.vls.windowStatusDriverRear",
            state_mapping=WINDOW_STATUS,
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Window Status Passenger",
            "vehicle_shadow.vls.windowStatusPassenger",
            state_mapping=WINDOW_STATUS,
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Window Status Passenger Rear",
            "vehicle_shadow.vls.windowStatusPassengerRear",
            state_mapping=WINDOW_STATUS,
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Window Status Sunroof",
            "vehicle_shadow.vls.sunroofOpenStatus",
            state_mapping=SUNROOF_STATUS,
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Window Status Updated",
            "vehicle_shadow.vls.windowStatusDriverUpdatedAt",
        ),
    ]
    return sensors
