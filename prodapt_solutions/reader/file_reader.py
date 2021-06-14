
import os

from helper.logging_handler import log
from helper.enum_definitions import InputFormatEnum
from reader.unified_reader import InputReader
from config.application_config import FileReaderConfig

class FileReader(InputReader):

    def __init__(self, fileReaderConfig: FileReaderConfig = None):

        if fileReaderConfig is None:
            fileReaderConfig = FileReaderConfig
        filepath = fileReaderConfig.Filepath
        _, fileext = os.path.splitext(filepath)

        try:
            self.fileFormat = InputFormatEnum(fileext.lower())
        except:
            self.fileFormat = None

        self.filepath = filepath

    @property
    def file_format(self):

        return self.__fileFormat

    @file_format.setter
    def file_format(self):

        log.error("Write operation is not allowed for file_format")

    @file_format.deleter
    def file_format(self):

        log.error("Delete operation is not allowed for file_format")

    def readblock(self, size: int = 1024):
        pass

    def readone(self):
        pass

    def readall(self):
        
        return open(self.filepath).read()
