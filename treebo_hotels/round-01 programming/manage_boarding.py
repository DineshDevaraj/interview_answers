
from hotel_detail import PreferredAllocation
from exceptions_definition import RoomAlreadyEmpty

class ManageBoarding:

    @staticmethod
    def check_in(hotelDetail, numberOfRoom):

        roomList = []
        roomsAllocated = 0

        if numberOfRoom > (hotelDetail.maxRooms - hotelDetail.roomsTaken):
            raise CannotAllocate()

        if hotelDetail.preferedAlloc == PreferredAllocation.TopDown:
            it = reversed(range(hotelDetail.numberOfFloor))
        else: # hotelDetail.preferedAlloc == PreferredAllocation.BottomUp:
            it = range(hotelDetail.numberOfFloor)

        breakOuter = False
        for floorNumber in it:

            for roomNumber in range(hotelDetail.roomsPerFloor):

                if hotelDetail.roomsAvailablity[floorNumber][roomNumber] == 1:
                    continue

                # __import__("pdb").set_trace()
                hotelDetail.roomsAvailablity[floorNumber][roomNumber] = 1
                hotelDetail.lastAllocatedRoom = (floorNumber, roomNumber)
                roomList.append((floorNumber, roomNumber))
                hotelDetail.roomsTaken += 1
                roomsAllocated += 1
                
                if roomsAllocated == numberOfRoom:
                    breakOuter = True
                    break
                
            if breakOuter == True:
                break

        else:

            raise CannotAllocateRoom()

        return roomList

    @staticmethod
    def check_out(hotelDetail, roomNumberList):

        # __import__("pdb").set_trace()
        for floorNumber, roomNumber in roomNumberList:
            if hotelDetail.roomsAvailablity[floorNumber][roomNumber] == 0:
                raise RoomAlreadyEmpty()
            hotelDetail.roomsAvailablity[floorNumber][roomNumber] = 0
            hotelDetail.roomsTaken -= 1
