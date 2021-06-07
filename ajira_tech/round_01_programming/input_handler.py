
import ast

from abc import ABC,abstractmethod

from terrain_properties import TerrainTypes
from soldier_properties import PlatoonClass
from soldier_properties import UnitAdvantageFactor

from exceptions_definition import InvalidInput
from exceptions_definition import ArgumentError

class InputHandler(ABC) :

    @abstractmethod
    def get_all_input():
        pass

    @abstractmethod
    def get_single_input():
        pass

    @staticmethod
    def get_non_empty_lines(stringData):

        nonEmptyLines = []

        for line in stringData.splitlines():
            line = line.strip()
            if line == "": continue
            nonEmptyLines.append(line)

        return nonEmptyLines

    @staticmethod
    def parse_input(selfPlatoonListString, opponentPlatoonListString,
            unitAdvantageFactorListString, terrainListString):

        selfPlatoonList = []
        for platoonInfo in selfPlatoonListString.split(";"):
            (platoonClass, platoonStrength) = platoonInfo.split('#')
            selfPlatoonList.append((PlatoonClass(platoonClass), int(platoonStrength)))
        # print(selfPlatoonList)
        numberOfPlatoons = len(selfPlatoonList)

        opponentPlatoonList = []
        for platoonInfo in opponentPlatoonListString.split(";"):
            (platoonClass, platoonStrength) = platoonInfo.split('#')
            opponentPlatoonList.append((PlatoonClass(platoonClass), int(platoonStrength)))
        # print(opponentPlatoonList)
        if (len(opponentPlatoonList) != numberOfPlatoons):
            raise InvalidInput("Number of opponent platoon and your's should be equal")

        uafDict = {} # unitUnitAdvantageFactorDict
        for uafString in unitAdvantageFactorListString.split(";"):
            (platoonClass, unitAdvantageFactor) = uafString.split('#')
            uafDict[PlatoonClass(platoonClass)] = int(unitAdvantageFactor)
        # print(unitUnitAdvantageFactorDict)
        UnitAdvantageFactor.init(uafDict)

        terrainList = [TerrainTypes(x) for x in terrainListString.split(';')]
        if (len(terrainList) != numberOfPlatoons):
            raise InvalidInput("Number of terrains and number of platoon should be equal")

        return (selfPlatoonList, opponentPlatoonList, terrainList, numberOfPlatoons)

    @staticmethod
    def factory(inputChannelType, *varg):

        inputChannelType = inputChannelType.lower()

        if inputChannelType == "cli":

            return CliInputHandler()

        elif inputChannelType == "file":

            if len(varg) < 1:
                raise ArgumentError("Mandatory argument FilePath is missing")

            filePath = varg[0]
            # do all filePath validation here
            return FileInputHandler(filePath)

        if inputChannelType == "rest":

            if len(varg) < 1:
                raise ArgumentError("Mandatory argument PortNumber is missing")

            portNumber = varg[0]
            # do all portNumber validation here
            return RestInputHandler(portNumber)

class CliInputHandler(InputHandler):

    def __init__(self):

        pass

    def get_single_input(self):

        selfPlatoonListString = input("Please enter your platoon details: ")
        opponentPlatoonListString = input("Please enter opponent platoon details: ")
        unitAdvantageFactorListString = input("Please enter unit advantage factor: ")
        terrainListString = input("Please enter the terrain list: ")

        return InputHandler.parse_input(selfPlatoonListString, 
            opponentPlatoonListString, unitAdvantageFactorListString, 
                terrainListString)

    def get_all_input(self):

        while True:
            yield self.get_single_input()

class FileInputHandler(InputHandler):

    def __init__(self, filePath):

        self.filePath = filePath
        # do all file open error handling here
        self.getSingleInputCounter = 0

    def get_single_input(self):

        fileHandle = open(filePath)
        testSuite = ast.literal_eval(fileHandle.read())
        testCaseString = testSuite["list"][self.getSingleInputCounter]
        nonEmptyLines = InputHandler.get_non_empty_lines()
        testCaseTuple = InputHandler.parse_input(*nonEmptyLines)
        self.getSingleInputCounter += 1
        return testCase

    def get_all_input(self):

        with open(self.filePath) as fileHandle:
            testSuite = ast.literal_eval(fileHandle.read())
        for testCase in testSuite["list"]:
            nonEmptyLines = InputHandler.get_non_empty_lines(testCase)
            yield InputHandler.parse_input(*nonEmptyLines)

class RestInputHandler(InputHandler):

    def __init__(self, potNumber):

        self.portNumber = portNumber
        # todo: rest api connection

    def get_all_input(self):

        # todo
        pass

    def get_single_input(self):

        # todo
        pass
