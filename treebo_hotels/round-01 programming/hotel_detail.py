
from enum import Enum

class PreferredAllocation(Enum):

    TopDown = "TopDown"
    BottomUp = "BottomUp"

class HotelDetail:

    def __init__(self, hotelDetail):
    
        self.numberOfFloor = hotelDetail.get("numberOfFloor")
        self.roomsPerFloor = hotelDetail.get("roomsPerFloor")
        self.preferedAlloc = PreferredAllocation(hotelDetail.get("preferedAlloc"))

        self.roomsAvailablity = [0] * self.numberOfFloor
        for floorNumber in range(self.numberOfFloor):
            self.roomsAvailablity[floorNumber] = [0] * self.roomsPerFloor

        self.maxRooms = self.numberOfFloor * self.roomsPerFloor
        self.roomsTaken = 0
