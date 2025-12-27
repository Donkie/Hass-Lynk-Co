from .lynk_co_sensor import LynkCoSensor


# Dutch translations for alarm and SRS statuses
ALARM_STATUS = {
    "ALARM_STATUS_ARMED": "Ingeschakeld",
    "ALARM_STATUS_UNARMED": "Uitgeschakeld",
    "ALARM_STATUS_TRIGGERED": "Geactiveerd",
    "ALARM_STATUS_UNSPECIFIED": "Onbekend",
    "ALARM_STATUS_DATA_ARMED": "Ingeschakeld",
    "ALARM_STATUS_DATA_UNARMED": "Uitgeschakeld",
    "ALARM_ARMED": "Ingeschakeld",
    "ALARM_UNARMED": "Uitgeschakeld",
    "ALARM_TRIGGERED": "Geactiveerd",
    "ARMED": "Ingeschakeld",
    "UNARMED": "Uitgeschakeld",
    "TRIGGERED": "Geactiveerd",
}

SRS_STATUS = {
    "SRS_STATUS_OK": "OK",
    "SRS_STATUS_NOT_DEPLOYED": "Niet geactiveerd",
    "SRS_STATUS_DEPLOYED": "Geactiveerd",
    "SRS_STATUS_FAULT": "Storing",
    "SRS_STATUS_UNSPECIFIED": "Onbekend",
    "SRS_OK": "OK",
    "SRS_FAULT": "Storing",
    "NOT_DEPLOYED": "Niet geactiveerd",
    "DEPLOYED": "Geactiveerd",
    "OK": "OK",
    "FAULT": "Storing",
}


def create_sensors(coordinator, vin):
    sensors = [
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Last updated by car",
            "vehicle_record.updatedAt",
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Vehicle is running updated",
            "vehicle_shadow.bvs.engineStatusUpdatedAt",
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Vehicle Alarm Status",
            "vehicle_shadow.vls.alarmStatusData",
            state_mapping=ALARM_STATUS,
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co SRS Status",
            "vehicle_shadow.vrs.airbagStatus.srsStatus",
            state_mapping=SRS_STATUS,
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Airbag Status Updated At",
            "vehicle_shadow.vrs.airbagStatus.updatedAt",
        ),
    ]
    return sensors
