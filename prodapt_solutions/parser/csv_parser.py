
from csv import DictReader

from helper.logging_handler import log
from reader.unified_reader import InputReader
from parser.unified_parser import InputParser

class CsvParser(InputParser):
    
    def __init__(self, ipReader: InputReader, ipStructure: str):
        
        self.ipReader: InputReader = ipReader

    def trans(self, skip: int, count: int):
        pass
    
    def iterator(self, skip: int = 0, count: int = None):
        pass

    def __iter__(self):

        csvReader = DictReader(self.ipReader.read_all().split("\n"))
        log.debug(csvReader.fieldnames)
        for row in csvReader: yield row

    def __next__(self):

        """
            We create a generator in __iter__ hence no needed 
            to manage / terminate context in __next__
        """
        
        pass
