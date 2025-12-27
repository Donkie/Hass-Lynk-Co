from .lynk_co_sensor import LynkCoSensor


# Dutch translations for 12V battery statuses
BATTERY_CHARGE_STATUS = {
    "BATTERY_CHARGE_STATUS_CHARGING": "Laden",
    "BATTERY_CHARGE_STATUS_NOT_CHARGING": "Niet laden",
    "BATTERY_CHARGE_STATUS_OK": "OK",
    "BATTERY_CHARGE_STATUS_LOW": "Laag",
    "BATTERY_CHARGE_STATUS_UNSPECIFIED": "Onbekend",
    "CHARGING": "Laden",
    "NOT_CHARGING": "Niet laden",
    "CHARGE_OK": "OK",
    "CHARGE_LOW": "Laag",
    "OK": "OK",
    "LOW": "Laag",
}

BATTERY_HEALTH_STATUS = {
    "BATTERY_HEALTH_STATUS_OK": "OK",
    "BATTERY_HEALTH_STATUS_GOOD": "Goed",
    "BATTERY_HEALTH_STATUS_FAIR": "Matig",
    "BATTERY_HEALTH_STATUS_POOR": "Slecht",
    "BATTERY_HEALTH_STATUS_CRITICAL": "Kritiek",
    "BATTERY_HEALTH_STATUS_UNSPECIFIED": "Onbekend",
    "HEALTH_OK": "OK",
    "HEALTH_GOOD": "Goed",
    "HEALTH_FAIR": "Matig",
    "HEALTH_POOR": "Slecht",
    "HEALTH_CRITICAL": "Kritiek",
    "OK": "OK",
    "GOOD": "Goed",
    "POOR": "Slecht",
}

BATTERY_LEVEL_STATUS = {
    "BATTERY_POWER_LEVEL_STATUS_OK": "OK",
    "BATTERY_POWER_LEVEL_STATUS_LOW": "Laag",
    "BATTERY_POWER_LEVEL_STATUS_CRITICAL": "Kritiek",
    "BATTERY_POWER_LEVEL_STATUS_UNSPECIFIED": "Onbekend",
    "BATTERY_ENERGY_LEVEL_STATUS_OK": "OK",
    "BATTERY_ENERGY_LEVEL_STATUS_LOW": "Laag",
    "BATTERY_ENERGY_LEVEL_STATUS_CRITICAL": "Kritiek",
    "BATTERY_ENERGY_LEVEL_STATUS_UNSPECIFIED": "Onbekend",
    "LEVEL_OK": "OK",
    "LEVEL_LOW": "Laag",
    "LEVEL_CRITICAL": "Kritiek",
    "OK": "OK",
    "LOW": "Laag",
}


def create_sensors(coordinator, vin):
    sensors = [
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co 12V Battery",
            "vehicle_record.battery.chargeLevel",
            "%",
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co 12V Battery Charge",
            "vehicle_record.battery.charge",
            state_mapping=BATTERY_CHARGE_STATUS,
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co 12V Battery Health",
            "vehicle_record.battery.health",
            state_mapping=BATTERY_HEALTH_STATUS,
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co 12V Battery Power level",
            "vehicle_record.battery.powerLevel",
            state_mapping=BATTERY_LEVEL_STATUS,
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co 12V Battery Energy level",
            "vehicle_record.battery.energyLevel",
            state_mapping=BATTERY_LEVEL_STATUS,
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co 12V Battery Voltage",
            "vehicle_record.battery.voltage",
        ),
    ]
    return sensors
