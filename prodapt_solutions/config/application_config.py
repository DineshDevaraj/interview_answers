
import sys
import logging

from abc import ABC
from dataclasses import dataclass
from helper.enum_definitions import DBMSNameEnum
from helper.enum_definitions import LoggingDestinationEnum

@dataclass
class LoggingConfig:

    Stream = sys.stdout
    
    Filepath = "./logs/evalsr.log"
    MaxBytes = 8*1024*1024
    BackupCount = 10
    Level = logging.INFO
    
    Destination = LoggingDestinationEnum.Console

class InputReaderConfig(ABC):
    pass

@dataclass
class DBReaderConfig(InputReaderConfig):

    Url: str = ""
    Username: str = ""
    Password: str = ""
    DBMSName = DBMSNameEnum.Mongo
    DBName = "TransRecord"

@dataclass
class RestReaderConfig(InputReaderConfig):

    ListenHost: str = ""
    ListenPort: int = 0

@dataclass
class FileReaderConfig(InputReaderConfig):

    Filepath: str = "input_files/trans_history.csv"
