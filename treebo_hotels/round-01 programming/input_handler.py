
from abc import ABC,abstractmethod

from customer_actions import Actions

class InputParam:

    pass

class InputHandler(ABC):

    @staticmethod
    def factory(inputMethod):

        inputMethod = inputMethod.lower()
        if inputMethod == "cli":
            return CliInputHandler()

    @abstractmethod
    def get_input(): pass

class CliInputHandler:

    def get_input(self):

        inputParam = InputParam()

        while True:

            print("Enter 1 for check-in")
            print("Enter 2 for check-out")
            choice = input("What do you want to do? ")

            if choice == "1":

                numberOfRoom = int(input("How many rooms do you want? "))
                inputParam.numberOfRoom = numberOfRoom
                inputParam.action = Actions("CheckIn")

            elif choice == "2":

                roomList = []
                print("Which all rooms do you want to check-out?")
                print("Enter the room numbers seperated by space")

                for roomNumberString in input().split():

                    # we can do input validation here
                    (floorNumber, roomNumber) = roomNumberString.split(".")
                    roomList.append((int(floorNumber), int(roomNumber)))

                inputParam.action = Actions("CheckOut")
                inputParam.roomList = roomList

            elif choice == "Q" or choice == "q":

                exit(-1)

            else:

                print(f"Ivalid choice {choice}")
                continue

            yield inputParam
