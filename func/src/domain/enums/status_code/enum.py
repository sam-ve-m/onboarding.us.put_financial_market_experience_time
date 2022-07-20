# STANDARD IMPORTS
from enum import IntEnum


class InternalCode(IntEnum):
    SUCCESS = 0
    INVALID_PARAMS = 10
    JWT_INVALID = 30
    INTERNAL_SERVER_ERROR = 100
    NOT_SENT_TO_PERSEPHONE = 60
    INVALID_BR_ONBOARDING_STEP = 109
    INVALID_US_ONBOARDING_STEP = 49
    UNIQUE_ID_WAS_NOT_UPDATED = 69
    HTTP_CONNECTION_POLL = 79

    def __repr__(self):
        return self.value
