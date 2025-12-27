from .lynk_co_sensor import LynkCoSensor


# Dutch translations for door/lock statuses
DOOR_LOCK_STATUS = {
    "DOOR_LOCKS_STATUS_LOCKED": "Vergrendeld",
    "DOOR_LOCKS_STATUS_UNLOCKED": "Ontgrendeld",
    "DOOR_LOCKS_STATUS_SAFE_LOCKED": "Veilig vergrendeld",
    "DOOR_LOCKS_STATUS_UNSPECIFIED": "Onbekend",
}

DOOR_OPEN_STATUS = {
    # New pattern with full prefix
    "DOOR_OPEN_STATUS_CLOSED": "Dicht",
    "DOOR_OPEN_STATUS_OPEN": "Open",
    "DOOR_OPEN_STATUS_AJAR": "Op een kier",
    "DOOR_OPEN_STATUS_UNSPECIFIED": "Onbekend",
    # Old pattern fallback
    "DOOR_CLOSED": "Dicht",
    "DOOR_OPEN": "Open",
    "DOOR_AJAR": "Op een kier",
    "CLOSED": "Dicht",
    "OPEN": "Open",
    "AJAR": "Op een kier",
}

TRUNK_STATUS = {
    "TRUNK_OPEN_STATUS_CLOSED": "Dicht",
    "TRUNK_OPEN_STATUS_OPEN": "Open",
    "TRUNK_OPEN_STATUS_AJAR": "Op een kier",
    "TRUNK_OPEN_STATUS_UNSPECIFIED": "Onbekend",
    "TRUNK_CLOSED": "Dicht",
    "TRUNK_OPEN": "Open",
    "TRUNK_AJAR": "Op een kier",
    "CLOSED": "Dicht",
    "OPEN": "Open",
}

ENGINE_HOOD_STATUS = {
    "ENGINE_HOOD_STATUS_CLOSED": "Dicht",
    "ENGINE_HOOD_STATUS_OPEN": "Open",
    "ENGINE_HOOD_STATUS_UNSPECIFIED": "Onbekend",
    "ENGINE_HOOD_CLOSED": "Dicht",
    "ENGINE_HOOD_OPEN": "Open",
    "CLOSED": "Dicht",
    "OPEN": "Open",
}

LOCK_STATUS = {
    "DOOR_LOCK_STATUS_LOCKED": "Vergrendeld",
    "DOOR_LOCK_STATUS_UNLOCKED": "Ontgrendeld",
    "DOOR_LOCK_STATUS_UNSPECIFIED": "Onbekend",
    "LOCKED": "Vergrendeld",
    "UNLOCKED": "Ontgrendeld",
}


def create_sensors(coordinator, vin):
    sensors = [
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Door lock status",
            "vehicle_shadow.vls.doorLocksStatus",
            state_mapping=DOOR_LOCK_STATUS,
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Door Trunk Status",
            "vehicle_shadow.vls.trunkOpenStatus",
            state_mapping=TRUNK_STATUS,
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Door Engine Hood Status",
            "vehicle_shadow.vls.engineHoodStatus",
            state_mapping=ENGINE_HOOD_STATUS,
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Door lock Updated",
            "vehicle_shadow.vls.doorLocksUpdatedAt",
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Door Open Status Driver",
            "vehicle_shadow.vls.doorOpenStatusDriver",
            state_mapping=DOOR_OPEN_STATUS,
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Door Open Status Driver Rear",
            "vehicle_shadow.vls.doorOpenStatusDriverRear",
            state_mapping=DOOR_OPEN_STATUS,
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Door Open Status Passenger",
            "vehicle_shadow.vls.doorOpenStatusPassenger",
            state_mapping=DOOR_OPEN_STATUS,
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Door Open Status Passenger Rear",
            "vehicle_shadow.vls.doorOpenStatusPassengerRear",
            state_mapping=DOOR_OPEN_STATUS,
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Door Lock Status Driver",
            "vehicle_shadow.vls.doorLockStatusDriver",
            state_mapping=LOCK_STATUS,
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Door Lock Status Driver Rear",
            "vehicle_shadow.vls.doorLockStatusDriverRear",
            state_mapping=LOCK_STATUS,
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Door Lock Status Passenger",
            "vehicle_shadow.vls.doorLockStatusPassenger",
            state_mapping=LOCK_STATUS,
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Door Lock Status Passenger Rear",
            "vehicle_shadow.vls.doorLockStatusPassengerRear",
            state_mapping=LOCK_STATUS,
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Central Locking Updated At",
            "vehicle_shadow.vls.centralLockingUpdatedAt",
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Sunroof Updated At",
            "vehicle_shadow.vls.sunroofUpdatedAt",
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Tank Flap Updated At",
            "vehicle_shadow.vls.tankFlapUpdatedAt",
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Alarm Status Updated At",
            "vehicle_shadow.vls.alarmStatusUpdatedAt",
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Trunk Open Updated At",
            "vehicle_shadow.vls.trunkOpenUpdatedAt",
        ),
        LynkCoSensor(
            coordinator,
            vin,
            "Lynk & Co Engine Hood Updated At",
            "vehicle_shadow.vls.engineHoodUpdatedAt",
        ),
    ]
    return sensors
