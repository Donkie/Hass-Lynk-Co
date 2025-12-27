from .lynk_co_sensor import LynkCoSensor


# Dutch translations for seatbelt statuses
SEATBELT_STATUS = {
    "SEATBELT_STATUS_FASTENED": "Vast",
    "SEATBELT_STATUS_UNFASTENED": "Los",
    "SEATBELT_STATUS_UNSPECIFIED": "Onbekend",
    "SEATBELT_FASTENED": "Vast",
    "SEATBELT_UNFASTENED": "Los",
    "FASTENED": "Vast",
    "UNFASTENED": "Los",
    True: "Vast",
    False: "Los",
}


def create_sensors(coordinator, vin):
    sensors = [
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Driver Seatbelt Status",
            "vehicle_shadow.vrs.seatBeltStatus.driver.fastened",
            state_mapping=SEATBELT_STATUS,
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Driver Rear Seatbelt Status",
            "vehicle_shadow.vrs.seatBeltStatus.driverRear.fastened",
            state_mapping=SEATBELT_STATUS,
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Passenger Seatbelt Status",
            "vehicle_shadow.vrs.seatBeltStatus.passenger.fastened",
            state_mapping=SEATBELT_STATUS,
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Passenger Rear Seatbelt Status",
            "vehicle_shadow.vrs.seatBeltStatus.passengerRear.fastened",
            state_mapping=SEATBELT_STATUS,
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Mid Rear Seatbelt Status",
            "vehicle_shadow.vrs.seatBeltStatus.midRear.fastened",
            state_mapping=SEATBELT_STATUS,
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Seatbelt Status Updated At",
            "vehicle_shadow.vrs.seatBeltStatus.updatedAt",
        ),
    ]
    return sensors
