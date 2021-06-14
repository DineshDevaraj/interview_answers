
from abc import ABC
from abc import abstractmethod

from reader.unified_reader import InputReader
from helper.enum_definitions import InputFormatEnum

class InputParser(ABC):

    @staticmethod
    def factory(ipReader: InputReader, ipFormat: InputFormatEnum, 
            ipStructure: str = None):

        inputParser = None

        match ipFormat:

            case InputFormatEnum.CSV:

                from parser.csv_parser import CsvParser
                inputParser = CsvParser(ipReader, ipStructure)

            case InputFormatEnum.JSON:

                from parser.json_parser import JsonParser
                inputParser = JsonParser(ipReader, ipStructure)

            case _: # InputFormatEnum.XML

                from parser.xml_parser import XmlParser
                inputParser = XmlParser(ipReader, ipStructure)

        return inputParser

    @abstractmethod
    def trans(self, skip: int, count: int):

        """
            read_trans: read the <count> number of trans

            skip  : number of transactions that you want to skip
            count : number of transactions that you want to read

            example on how to read frist 1000 transaction

            batchSize = 100
            for I in range(10):
                dbReader.read_trans(I*batchSize, batchSize)
        """

        pass

    @abstractmethod
    def iterator(self, skip: int = 0, count: int = None):

        """
            iterator : allows to iterate over each trans

            skip  : number of transactions that you want to skip

            count : number of transactions that you want to read

                    If this value is not specified the the iterator
                    will read one-by-one all the transactions in case
                    of file and database.

                    In case of resta-api this will be an infinite loop
                    that will recv from clients
        """

        pass

    def __iter__(self):

        """
            __iter__: same as calling iterator with default arguments
        """

        return self.iterator()

    @abstractmethod
    def __next__(self):
        pass
