from enum import Enum


class StatusCodes(Enum):
    DATA_READ_SUCCESS="DATA READ SUCCESS"
    DATA_READ_FAILURE = "DATA READ FAILURE"
    DATA_INSERT_SUCCESS = "DATA INSERT SUCCESS"
    DATA_INSERT_FAILURE = "DATA INSERT FAILURE"
    DATA_DELETE_SUCCESS = "DATA DELETE SUCCESS"
    DATA_DELETE_FAILURE = "DATA DELETE FAILURE"


class ProcessingType(Enum):
    INSERT = "INSERT"
    DELETE = "DELETE"
    READ = "READ"


class ResponseStatus(Enum):
    SUCCESS = "SUCCESS"
    ERROR = "ERROR"

