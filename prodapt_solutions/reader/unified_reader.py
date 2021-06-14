
from abc import ABC
from enum import Enum
from abc import abstractmethod
from helper.enum_definitions import InputMethodEnum
from config.application_config import InputReaderConfig

class InputReader(ABC):

    @staticmethod
    def factory(ipMethod: InputMethodEnum, inputReaderConfig: InputReaderConfig):

        inputReader = None

        match ipMethod:

            case InputMethodEnum.DB:

                from reader.db_reader import DBReader
                inputReader = DBReader.factory(inputReaderConfig)

            case InputMethodEnum.REST:

                from reader.rest_reader import RestReader
                inputReader = RestReader(inputReaderConfig)

            case _: # InputMethodEnum.FILE:

                from reader.file_reader import FileReader
                inputReader = FileReader(inputReaderConfig)

        return inputReader

    @abstractmethod
    def read_block(self, size: int = 1024):

        """
            if InputMethod is File:
                Read given size of data if input method is file
            elif InputMethod is NoSQL:
                Read multiple documents until the total size is greater than given size 
            elif InputMethod is SQL:
                Read multiple rows until the total size is greater than given size
            else: # InputMethod is REST:
                Recv until the total size is greater than given size

            Note: The offset is internally auto increamented. So for each call the 
                  next block of data will be returned
        """

        pass

    @abstractmethod
    def read_one(self):

        """
            if InputMethod is File:
                Read single line
            elif InputMethod is NoSQL:
                Read single document
            elif InputMethod is SQL:
                Read single row
            else: # InputMethod is REST:
                Read till new line

            Note: The offset is internally auto increamented. So for each call the 
                  next line of data will be returned
        """
        pass

    @abstractmethod
    def read_all(self):

        """
            if InputMethod is File:
                Read the entire file
            elif InputMethod is NoSQL:
                Read all documents in the collection
            elif InputMethod is SQL:
                Read all rows in the database
            else: # InputMethod is REST:
                Recv until socket-close or end-delimter
        """
        pass