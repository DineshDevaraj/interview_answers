
from enum import Enum
from soldier_properties import PlatoonClass

class TerrainTypes(Enum):

    Hill = "Hill"
    Plains = "Plains"
    Muddy = "Muddy"
    Default = "Default"

# nested dictionary
TerrainStrengthDict = {

    TerrainTypes.Hill: {
        PlatoonClass.CavalryArcher: 2,
        PlatoonClass.FootArcher: 2,
        PlatoonClass.Militia: 0.5,
        PlatoonClass.Spearmen: 0.5,
        PlatoonClass.LightCavalry: 0.5,
        PlatoonClass.HeavyCavalry: 0.5,
    },

    TerrainTypes.Plains: {
        PlatoonClass.CavalryArcher: 2,
        PlatoonClass.LightCavalry: 2,
        PlatoonClass.HeavyCavalry: 2
    },

    TerrainTypes.Muddy: {
        PlatoonClass.FootArcher: 2,
        PlatoonClass.Militia: 2,
        PlatoonClass.Spearmen: 2
    },

    TerrainTypes.Default: {
        # nothing here for now
    }

}

class TerrainAdvantageFactor:

    @staticmethod
    def value(terrainType, platoonClass):
        return TerrainStrengthDict[terrainType] \
                .get(platoonClass, 1)
