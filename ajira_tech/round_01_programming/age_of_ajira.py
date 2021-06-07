
#
# Name: Dinesh
# Mobile: 9080410470
# EmailId: dineshdevarajece@gmail.com
# Created: 22/May/2021
# Updated: 25/May/2021
#

from input_handler import InputHandler
from battle_strategy import StrategySelector
from exceptions_definition import InvalidInput
from exceptions_definition import ArgumentError
from exceptions_definition import WinningNotPossible

def main():

    try:

        i = 1
        testSuitePath = "test-suites/test-suite-2.py"

        # you can also replace the following
        # factory with FileInputHandler instanciation
        input_handler = InputHandler.factory("File", testSuitePath)
        # input_handler = InputHandler.factory("CLI", "test-suite.py")

        for (selfPlatoonList, opponentPlatoonList, terrainList,
            numberOfPlatoons) in input_handler.get_all_input():

            print("Test Case %02d" % (i))

            strategySelector = StrategySelector(selfPlatoonList, opponentPlatoonList,
                    terrainList, numberOfPlatoons)
            winning_combination, battle_index = strategySelector.winning_combination()

            print(";".join(map(lambda x:f"{x[0].value}#{x[1]}", winning_combination)))

            if battle_index != -1:

                artillerySupportRepr = ['.'] * numberOfPlatoons
                artillerySupportRepr[battle_index] = 'A'
                print(''.join(artillerySupportRepr))

            print()

            i += 1

    except WinningNotPossible as ex:

        print("There is no chance of winning")

    except (ArgumentError, InvalidInput) as ex:

        print(ex)

if __name__ == "__main__":

    main()
