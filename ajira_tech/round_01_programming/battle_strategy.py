
import math

from itertools import permutations

from soldier_properties import PlatoonClass
from soldier_properties import UnitAdvantageFactor
from soldier_properties import UnitAdvantageMapping

from terrain_properties import TerrainTypes
from terrain_properties import TerrainAdvantageFactor

from exceptions_definition import WinningNotPossible

class StrategySelector:

    ArtilleryStrength = 50

    def __init__(self, selfPlatoonList, opponentPlatoonList,
            terrainList, numberOfPlatoons):

        self.selfPlatoonList = selfPlatoonList
        self.opponentPlatoonList = opponentPlatoonList
        self.terrainList = terrainList
        self.numberOfPlatoons = numberOfPlatoons

        self.winWithArtilleryCombination = None

        # used only for debug print
        self.winWithArtilleryBattleStatus = None
        self.battleStatusList = None

    # def calculate_terrain_advantage_weighted_strength():
    # this name is too lengthy so using following name
    def calc_taws(self, platoonClass, platoonStrength, terrainType):

        terrainAdvantageFactor = TerrainAdvantageFactor \
            .value(terrainType, platoonClass)
        return platoonStrength * terrainAdvantageFactor

    # def calculate_unit_advantage_weighted_strength():
    # this name is too lengthy so using following name
    def calc_uaws(self, lhsPlatoonClass, rhsPlatoonClass, presentStrength):

        """
        this function tells if lhsPlatoonClass had any advantage over
        rhsPlatoonClass
        """

        if rhsPlatoonClass in UnitAdvantageMapping[lhsPlatoonClass]:

            unitUnitAdvantageFactor = UnitAdvantageFactor.value(lhsPlatoonClass)
            return presentStrength * unitUnitAdvantageFactor

        return presentStrength

    def validate_combination(self, combination):

        numberOfBattlesWon = 0
        self.battleStatusList = []
        canWinBattleWithArtillery = False

        for i in range(0, self.numberOfPlatoons):

            terrainType = self.terrainList[i]

            selfPlatoonClass = combination[i][0]
            selfPlatoonStrength = combination[i][1]

            opponentPlatoonClass = self.opponentPlatoonList[i][0]
            opponentPlatoonStrength = self.opponentPlatoonList[i][1]

            tawsSelf = self.calc_taws(selfPlatoonClass,
                selfPlatoonStrength, terrainType)
            tawsOpponent = self.calc_taws(opponentPlatoonClass,
                opponentPlatoonStrength, terrainType)

            uawsSelf = self.calc_uaws(selfPlatoonClass,
                opponentPlatoonClass, tawsSelf)
            uawsOpponent = self.calc_uaws(opponentPlatoonClass,
                selfPlatoonClass, tawsOpponent)

            if uawsSelf > uawsOpponent:

                self.battleStatusList.append((selfPlatoonClass.value,
                        selfPlatoonStrength, 1))
                numberOfBattlesWon += 1

            else:

                self.battleStatusList.append((selfPlatoonClass.value,
                        selfPlatoonStrength, 0))

                if  canWinBattleWithArtillery == False:

                    reducedOpponentPlatoonStrength = opponentPlatoonStrength \
                        - StrategySelector.ArtilleryStrength
                    reducedOpponentWeightedStrength = reducedOpponentPlatoonStrength \
                        * TerrainAdvantageFactor.value(terrainType, opponentPlatoonClass)
                    if reducedOpponentWeightedStrength < uawsSelf:
                        self.winWithArtilleryCombination = (combination, i)
                        canWinBattleWithArtillery = True

        # for-block end

        return numberOfBattlesWon, canWinBattleWithArtillery

    def winning_combination(self):

        canWinWarWithArtillery = False
        battleWinThresold = math.floor(self.numberOfPlatoons/2)

        for combination in permutations(self.selfPlatoonList):

            (numberOfBattlesWon, canWinBattleWithArtillery) = \
                self.validate_combination(combination)

            if numberOfBattlesWon > battleWinThresold:

                # print(battleStatusList)
                return combination, -1

            elif numberOfBattlesWon > (battleWinThresold-1) and \
                    canWinBattleWithArtillery == True:
                # create a deep copy
                self.winWithArtilleryBattleStatus = list(self.battleStatusList)
                canWinWarWithArtillery = True

        else: # for-else block

            if canWinWarWithArtillery == True:

                # print(self.winWithArtilleryBattleStatus)
                return self.winWithArtilleryCombination

            raise WinningNotPossible()
