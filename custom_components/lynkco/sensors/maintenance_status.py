from .lynk_co_sensor import LynkCoSensor


# Dutch translations for maintenance statuses
SERVICE_WARNING_STATUS = {
    "SERVICE_WARNING_STATUS_OK": "OK",
    "SERVICE_WARNING_STATUS_NORMAL": "Normaal",
    "SERVICE_WARNING_STATUS_REQUIRED": "Service nodig",
    "SERVICE_WARNING_STATUS_OVERDUE": "Service achterstallig",
    "SERVICE_WARNING_STATUS_UNSPECIFIED": "Onbekend",
    "SERVICE_WARNING_STATUS_NO_WARNING": "Geen waarschuwing",
    "SERVICE_WARNING_OK": "OK",
    "SERVICE_WARNING_REQUIRED": "Service nodig",
    "NO_WARNING": "Geen waarschuwing",
    "WARNING": "Waarschuwing",
    "NORMAL": "Normaal",
    "OK": "OK",
}

OIL_LEVEL_STATUS = {
    "ENGINE_OIL_LEVEL_STATUS_NORMAL": "Normaal",
    "ENGINE_OIL_LEVEL_STATUS_OK": "OK",
    "ENGINE_OIL_LEVEL_STATUS_LOW": "Laag",
    "ENGINE_OIL_LEVEL_STATUS_VERY_LOW": "Zeer laag",
    "ENGINE_OIL_LEVEL_STATUS_CRITICAL": "Kritiek",
    "ENGINE_OIL_LEVEL_STATUS_OVERFILLED": "Te vol",
    "ENGINE_OIL_LEVEL_STATUS_UNSPECIFIED": "Onbekend",
    "OIL_LEVEL_OK": "OK",
    "OIL_LEVEL_LOW": "Laag",
    "OIL_LEVEL_NORMAL": "Normaal",
    "LEVEL_OK": "OK",
    "LEVEL_LOW": "Laag",
    "NORMAL": "Normaal",
    "OK": "OK",
    "LOW": "Laag",
}

OIL_PRESSURE_STATUS = {
    "ENGINE_OIL_PRESSURE_STATUS_NORMAL": "Normaal",
    "ENGINE_OIL_PRESSURE_STATUS_OK": "OK",
    "ENGINE_OIL_PRESSURE_STATUS_LOW": "Laag",
    "ENGINE_OIL_PRESSURE_STATUS_CRITICAL": "Kritiek",
    "ENGINE_OIL_PRESSURE_STATUS_UNSPECIFIED": "Onbekend",
    "OIL_PRESSURE_OK": "OK",
    "OIL_PRESSURE_LOW": "Laag",
    "PRESSURE_OK": "OK",
    "PRESSURE_LOW": "Laag",
    "NORMAL": "Normaal",
    "OK": "OK",
    "LOW": "Laag",
}

WASHER_FLUID_STATUS = {
    "WASHER_FLUID_LEVEL_STATUS_OK": "OK",
    "WASHER_FLUID_LEVEL_STATUS_LOW": "Laag",
    "WASHER_FLUID_LEVEL_STATUS_EMPTY": "Leeg",
    "WASHER_FLUID_LEVEL_STATUS_NORMAL": "Normaal",
    "WASHER_FLUID_LEVEL_STATUS_UNSPECIFIED": "Onbekend",
    "WASHER_FLUID_OK": "OK",
    "WASHER_FLUID_LOW": "Laag",
    "WASHER_FLUID_EMPTY": "Leeg",
    "LEVEL_OK": "OK",
    "LEVEL_LOW": "Laag",
    "OK": "OK",
    "LOW": "Laag",
    "NORMAL": "Normaal",
}


def create_sensors(coordinator, vin):
    sensors = [
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Distance To Service",
            "vehicle_record.maintenanceStatus.distanceToService",
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Days To Service",
            "vehicle_record.maintenanceStatus.daysToService",
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Engine Hours To Service",
            "vehicle_record.maintenanceStatus.engineHoursToService",
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Engine Coolant Temperature",
            "vehicle_record.maintenanceStatus.engineCoolantTemperature",
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Service Warning Status",
            "vehicle_record.maintenanceStatus.serviceWarningStatus",
            state_mapping=SERVICE_WARNING_STATUS,
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Engine Oil Level Status",
            "vehicle_record.maintenanceStatus.engineOilLevelStatus",
            state_mapping=OIL_LEVEL_STATUS,
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Engine Oil Pressure Status",
            "vehicle_record.maintenanceStatus.engineOilPressureStatus",
            state_mapping=OIL_PRESSURE_STATUS,
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Washer Fluid Level Status",
            "vehicle_record.maintenanceStatus.washerFluidLevelStatus",
            state_mapping=WASHER_FLUID_STATUS,
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Maintenance Status Updated",
            "vehicle_record.maintenanceStatus.vehicleUpdatedAt",
        ),
    ]
    return sensors
