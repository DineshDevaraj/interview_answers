
import logging
from config.cliargs import CliArgs
from config.bank_config import BankConfig
from helper.enum_definitions import InputMethodEnum
from config.application_config import LoggingConfig
from config.application_config import FileReaderConfig


"""
    The higherarchy of configurations are in the following order
    First one has lowest priority and last one has highest priority
    application_config -> bank_config_dict -> cliargs
"""

def chain_bank_config(bankConfig: BankConfig):

    if CliArgs.InputFilepath is not None:
        bankConfig.update(
            InputMethod = InputMethodEnum.File,
            InputReaderConfig = FileReaderConfig(
                CliArgs.InputFilepath
            )
        )

    return bankConfig

def chain_logging_config():
    
    if CliArgs.LogLevel is not None:
        LoggingConfig.Level = logging.getLevelName(
            CliArgs.LogLevel
        )
