
import sys
import logging

from helper.metaclasses_definition import Singleton
from config.application_config import LoggingConfig
from config.application_config import LoggingDestinationEnum

from logging.handlers import RotatingFileHandler

def init_logger():

    logger = logging.getLogger(__name__)
    logger.setLevel(LoggingConfig.Level)
    
    if LoggingConfig.Destination == LoggingDestinationEnum.File:
        destHandler = RotatingFileHandler(
            LoggingConfig.Filepath, 
            maxBytes=LoggingConfig.MaxBytes, 
            backupCount=LoggingConfig.BackupCount
        )
    else:
        destHandler = logging.StreamHandler()
    
    format = '%(asctime)s - %(module)s:%(lineno)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(format)
    destHandler.setFormatter(formatter)
    logger.addHandler(destHandler)

    return logger

log = init_logger()
