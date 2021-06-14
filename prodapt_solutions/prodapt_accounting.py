
from config.application_config import LoggingConfig
from mapping.unified_fields import UnifiedFieldsConvertor
from parser.unified_parser import InputParser
from reader.unified_reader import InputReader
from config.cliargs import CliArgs
from helper.enum_definitions import InputMethodEnum
from config.banks_config_dict import BanksConfigDict
from config.chain_config import chain_logging_config
from config.chain_config import chain_bank_config

def main():

    CliArgs.init()
    chain_logging_config()

    bankName = CliArgs.BankName
    bankConfig = chain_bank_config(BanksConfigDict[bankName])

    ipReader = InputReader.factory(bankConfig.InputMethod, 
        bankConfig.InputReaderConfig)
    ipParser = InputParser.factory(ipReader, bankConfig.InputFormat)
    ufc = UnifiedFieldsConvertor(bankConfig)

    for trans in ipParser: print(ufc.convert(trans))

if __name__ == "__main__":

    main()
