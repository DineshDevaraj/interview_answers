
import sys

class Config:

    @staticmethod
    def init():

        # do needed validations here
        Config.hotelName = sys.argv[1]
