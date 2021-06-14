
from config.cliargs import CliArgs
from parser.unified_parser import InputParser
from reader.unified_reader import InputReader
from config.banks_config_dict import BanksConfigDict
from mapping.unified_fields import UnifiedFieldsConvertor

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
