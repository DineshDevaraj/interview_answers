
from enum import Enum
from metaclasses_definition import Singleton

class PlatoonClass(Enum):

    Militia = "Militia"
    Spearmen = "Spearmen"
    LightCavalry = "LightCavalry"
    HeavyCavalry = "HeavyCavalry"
    CavalryArcher = "CavalryArcher"
    FootArcher = "FootArcher"

UnitAdvantageMapping = {

    PlatoonClass.Militia : [
        PlatoonClass.Spearmen,
        PlatoonClass.LightCavalry
    ],

    PlatoonClass.Spearmen : [
        PlatoonClass.LightCavalry,
        PlatoonClass.HeavyCavalry
    ],

    PlatoonClass.LightCavalry : [
        PlatoonClass.FootArcher,
        PlatoonClass.CavalryArcher
    ],

    PlatoonClass.HeavyCavalry : [
        PlatoonClass.Militia,
        PlatoonClass.FootArcher,
        PlatoonClass.LightCavalry
    ],

    PlatoonClass.CavalryArcher : [
        PlatoonClass.Spearmen,
        PlatoonClass.HeavyCavalry
    ],

    PlatoonClass.FootArcher : [
        PlatoonClass.Militia,
        PlatoonClass.CavalryArcher
    ]

}

class UnitAdvantageFactor(metaclass=Singleton):

    __advantageFactorDict = None

    @staticmethod
    def init(advantageFactorDict):

        UnitAdvantageFactor.__advantageFactorDict = advantageFactorDict

    @staticmethod
    def value(platoonClass):

        return UnitAdvantageFactor.__advantageFactorDict.get(platoonClass, 1)
