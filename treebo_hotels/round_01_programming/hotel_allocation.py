
import ast 

from configurations import Config
from hotel_detail import HotelDetail
from customer_actions import Actions
from input_handler import InputHandler
from manage_boarding import ManageBoarding

def main():

    Config.init()
    
    # fh - fileHandle
    fhHotelDetail = open("hotels_catalog.py")
    hotelsDetailDict = ast.literal_eval(fhHotelDetail.read())
    hotelDetailInst = HotelDetail(hotelsDetailDict[Config.hotelName])

    inputHandler = InputHandler.factory("CLI")

    # print(hotelDetailInst.roomsAvailablity)
    for inputParam in inputHandler.get_input():

        if inputParam.action == Actions.CheckIn:
            ManageBoarding.check_in(hotelDetailInst, inputParam.numberOfRoom)
        else: # inputParam.action == Actions.CheckOut
            ManageBoarding.check_out(hotelDetailInst, inputParam.roomList)
            
        print(hotelDetailInst.roomsAvailablity)

if __name__ == "__main__":

    main()
