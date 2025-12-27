from .lynk_co_sensor import LynkCoSensor


# Dutch translations for temperature quality
TEMP_QUALITY = {
    "TEMPERATURE_QUALITY_OK": "OK",
    "TEMPERATURE_QUALITY_GOOD": "Goed",
    "TEMPERATURE_QUALITY_POOR": "Slecht",
    "TEMPERATURE_QUALITY_UNKNOWN": "Onbekend",
    "TEMP_QUALITY_OK": "OK",
    "TEMP_QUALITY_GOOD": "Goed",
    "TEMP_QUALITY_POOR": "Slecht",
    "QUALITY_OK": "OK",
    "QUALITY_GOOD": "Goed",
    "QUALITY_POOR": "Slecht",
    "QUALITY_UNKNOWN": "Onbekend",
    "OK": "OK",
    "GOOD": "Goed",
    "POOR": "Slecht",
}


def create_sensors(coordinator, vin):
    sensors = [
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Interior Temperature",
            "vehicle_record.climate.interiorTemp.temp",
            "°C",
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Interior Temperature Quality",
            "vehicle_record.climate.interiorTemp.Quality",
            state_mapping=TEMP_QUALITY,
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Interior Temperature Unit",
            "vehicle_record.climate.interiorTemp.Unit",
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Climate Updated",
            "vehicle_record.climate.vehicleUpdatedAt",
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Exterior temperature",
            "vehicle_record.climate.exteriorTemp.temp",
            "°C",
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Exterior Temperature Quality",
            "vehicle_record.climate.exteriorTemp.Quality",
            state_mapping=TEMP_QUALITY,
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Exterior Temperature Unit",
            "vehicle_record.climate.exteriorTemp.Unit",
        ),
    ]
    return sensors
