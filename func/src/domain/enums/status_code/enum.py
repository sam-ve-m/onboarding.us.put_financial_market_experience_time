# STANDARD IMPORTS
from enum import IntEnum


class InternalCode(IntEnum):
    SUCCESS = 0
    INVALID_PARAMS = 10
    JWT_INVALID = 30
    INTERNAL_SERVER_ERROR = 100
    RESPONSE_ERROR_DRIVE_WEALTH = 50
    NOT_SENT_TO_PERSEPHONE = 60
    NOT_DATE_TIME = 99
    INVALID_BR_ONBOARDING_STEP = 109
    INVALID_US_ONBOARDING_STEP = 49
    DATA_WAS_NOT_UPDATED_DRIVE_WEALTH = 59
    UNIQUE_ID_WAS_NOT_UPDATED = 69

    def __repr__(self):
        return self.value
