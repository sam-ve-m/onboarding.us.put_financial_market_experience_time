# STANDARD IMPORTS
from enum import Enum


class PersephoneQueue(Enum):
    PROSPECT_USER_QUEUE = 0
    TERM_QUEUE = 1
    SUITABILITY_QUEUE = 2
    KYC_TABLE_QUEUE = 3
    USER_IDENTIFIER_DATA = 4
    USER_SELFIE = 5
    USER_COMPLEMENTARY_DATA = 6
    USER_DOCUMENT = 7
    USER_POLITICALLY_EXPOSED_IN_US = 8
    USER_SET_ELECTRONIC_SIGNATURE = 9
    USER_CHANGE_OR_RESET_ELECTRONIC_SIGNATURE = 10
    USER_ELECTRONIC_SIGNATURE_SESSION = 11
    USER_UPDATE_REGISTER_DATA = 12
    USER_EXCHANGE_MEMBER_IN_US = 13
    USER_TRADE_TIME_EXPERIENCE_IN_US = 14
    USER_COMPANY_DIRECTOR_IN_US = 15
    USER_TAX_RESIDENCE_CONFIRMATION_US = 16
    USER_W8_CONFIRMATION_US = 17
    USER_EMPLOY_US = 18
    USER_THEBES_HALL = 0
    USER_AUTHENTICATION = 1
    USER_LOGOUT = 2
