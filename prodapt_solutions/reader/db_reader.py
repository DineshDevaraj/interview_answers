
from abc import ABC
from enum import Enum
from abc import abstractmethod

from logging_handler import log
from application_config import DBMSNameEnum
from application_config import DBReaderConfig
from reader.unified_reader import InputReader
from metaclasses_definition import SingletonAbstract

class DBConnection(metaclass=SingletonAbstract):

    c = None

    @abstractmethod
    def init():

        """
            init: initialize database connection
        """

        pass

    @staticmethod
    def factory(dbmsName: DBMSNameEnum):

        """
            factory: factory method to initialize database connection
        """

        match dbmsName:

            case DBMSNameEnum.Mongo:
                MongoConnection.init()
            case _: # DBMSName.MySQL
                MySQLConnection.init()

class MongoConnection(DBConnection):

    pass

class MySQLConnection(DBConnection):

    pass

class DBReader(InputReader):

    @staticmethod
    def factory():

        dbReader = None
        match DBReaderConfig.DBMSName:
            case DBMSNameEnum.Mongo:
                dbReader = MongoReader()
            case _: # DBMSName.MySQL
                dbReader = MySQLReader()
        return dbReader

class MongoReader(DBReader):

    def read_block(size: int = 1024):
        pass

    def read_one():
        pass

    def read_all():
        pass

class MySQLReader(DBReader):

    def read_block(size: int = 1024):
        pass

    def read_one():
        pass

    def read_all():
        pass
