from .lynk_co_sensor import LynkCoSensor


# Dutch translations for tyre statuses
TYRE_PRESSURE_STATUS = {
    "TYRE_PRESSURE_STATUS_OK": "OK",
    "TYRE_PRESSURE_STATUS_LOW": "Laag",
    "TYRE_PRESSURE_STATUS_HIGH": "Hoog",
    "TYRE_PRESSURE_STATUS_NO_WARNING": "Geen waarschuwing",
    "TYRE_PRESSURE_STATUS_WARNING": "Waarschuwing",
    "TYRE_PRESSURE_STATUS_VERY_LOW": "Zeer laag",
    "TYRE_PRESSURE_STATUS_FLAT": "Lek",
    "TYRE_PRESSURE_STATUS_NOT_MONITORED": "Niet gemonitord",
    "TYRE_PRESSURE_STATUS_UNSPECIFIED": "Onbekend",
    "TYRE_PRESSURE_OK": "OK",
    "TYRE_PRESSURE_LOW": "Laag",
    "TYRE_PRESSURE_HIGH": "Hoog",
    "TYRE_NOT_MONITORED": "Niet gemonitord",
    "NO_WARNING": "Geen waarschuwing",
    "WARNING": "Waarschuwing",
    "LOW_PRESSURE": "Lage druk",
    "HIGH_PRESSURE": "Hoge druk",
    "VERY_LOW_PRESSURE": "Zeer lage druk",
    "FLAT": "Lek",
    "PRESSURE_OK": "OK",
    "PRESSURE_LOW": "Laag",
    "PRESSURE_HIGH": "Hoog",
    "OK": "OK",
    "LOW": "Laag",
}


def create_sensors(coordinator, vin):
    tyre_sensors = [
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Driver Front Tyre Pressure",
            "vehicle_shadow.vrs.vehicleTyresStatus.driverFrontTyre.pressure",
            state_mapping=TYRE_PRESSURE_STATUS,
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Driver Rear Tyre Pressure",
            "vehicle_shadow.vrs.vehicleTyresStatus.driverRearTyre.pressure",
            state_mapping=TYRE_PRESSURE_STATUS,
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Passenger Front Tyre Pressure",
            "vehicle_shadow.vrs.vehicleTyresStatus.passengerFrontTyre.pressure",
            state_mapping=TYRE_PRESSURE_STATUS,
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Passenger Rear Tyre Pressure",
            "vehicle_shadow.vrs.vehicleTyresStatus.passengerRearTyre.pressure",
            state_mapping=TYRE_PRESSURE_STATUS,
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Tyres Status Updated At",
            "vehicle_shadow.vrs.vehicleTyresStatus.updatedAt",
        ),
    ]
    return tyre_sensors
