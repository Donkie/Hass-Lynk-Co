from .lynk_co_sensor import LynkCoSensor


# Dutch translations for fuel statuses
FUEL_LEVEL_STATUS = {
    "FUEL_LEVEL_STATUS_OK": "OK",
    "FUEL_LEVEL_STATUS_LOW": "Laag",
    "FUEL_LEVEL_STATUS_VERY_LOW": "Zeer laag",
    "FUEL_LEVEL_STATUS_CRITICAL": "Kritiek",
    "FUEL_LEVEL_STATUS_NORMAL": "Normaal",
    "FUEL_LEVEL_STATUS_UNSPECIFIED": "Onbekend",
    "FUEL_LEVEL_OK": "OK",
    "FUEL_LEVEL_LOW": "Laag",
    "OK": "OK",
    "LOW": "Laag",
    "NORMAL": "Normaal",
}

FUEL_TYPE = {
    "FUEL_TYPE_PETROL": "Benzine",
    "FUEL_TYPE_DIESEL": "Diesel",
    "FUEL_TYPE_ELECTRIC": "Elektrisch",
    "FUEL_TYPE_HYBRID": "Hybride",
    "FUEL_TYPE_PHEV": "Plug-in hybride",
    "FUEL_TYPE_UNSPECIFIED": "Onbekend",
    "PETROL": "Benzine",
    "DIESEL": "Diesel",
    "ELECTRIC": "Elektrisch",
    "HYBRID": "Hybride",
    "PHEV": "Plug-in hybride",
}

TANK_FLAP_STATUS = {
    "TANK_FLAP_STATUS_CLOSED": "Dicht",
    "TANK_FLAP_STATUS_OPEN": "Open",
    "TANK_FLAP_STATUS_UNSPECIFIED": "Onbekend",
    "TANK_FLAP_CLOSED": "Dicht",
    "TANK_FLAP_OPEN": "Open",
    "CLOSED": "Dicht",
    "OPEN": "Open",
}


def create_sensors(coordinator, vin):
    sensors = [
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Fuel Level",
            "vehicle_record.fuel.level",
            "liters",
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Fuel Updated",
            "vehicle_record.fuel.vehicleUpdatedAt",
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Fuel Level status",
            "vehicle_record.fuel.levelStatus",
            state_mapping=FUEL_LEVEL_STATUS,
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Fuel Type",
            "vehicle_record.fuel.fuelType",
            state_mapping=FUEL_TYPE,
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Fuel distance",
            "vehicle_record.fuel.distanceToEmpty",
            "km",
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Fuel avg consumption",
            "vehicle_record.fuel.averageConsumption",
            "L/100km",
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Fuel avg consumption latest cycle",
            "vehicle_record.fuel.averageConsumptionLatestDrivingCycle",
            "L/100km",
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Tank Flap Status",
            "vehicle_shadow.vls.tankFlapStatus",
            state_mapping=TANK_FLAP_STATUS,
        ),
    ]
    return sensors
