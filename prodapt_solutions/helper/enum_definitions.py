
from enum import Enum	
    
class DBMSNameEnum(Enum):

    Mongo = "mongo"
    MySQL = "mysql"

class InputMethodEnum(Enum):

    DB   = "db"
    REST = "rest"
    File = "file"

class InputFormatEnum(Enum):

    CSV  = ".csv"
    XML  = ".xml"
    JSON = ".json"

class LoggingDestinationEnum(Enum):

    File = 2
    Console = 1

class DatetimeFromatEnum(Enum):

    Split = "split"
    Join = "join"

class AmountFormatEnum(Enum):
    
    Split = "split"
    Join = "join"

class TransDirectionEnum(Enum):

    Remove = "remove"
    Add = "add"
