
import argparse

from helper.metaclasses_definition import Singleton

class CliArgs(metaclass=Singleton):

    BankName = None
    InputFilepath = None

    @staticmethod
    def init():

        my_parser = argparse.ArgumentParser()
        my_parser.add_argument('--bank-name', required=True)
        my_parser.add_argument('--input-filepath')
        args = my_parser.parse_args()

        CliArgs.BankName = args.bank_name
        CliArgs.InputFilepath = args.input_filepath
