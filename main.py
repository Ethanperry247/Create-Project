from logger import Logger
from send import Transceiver
from visualize import *
from alarm import *

log = Logger()
message = Transceiver()
alarm = Alarm()

def main():
    while True:
        pi_data = message()

        if (pi_data == 0):
        elif (pi_data == 1):
            alarm.sound_alarm()
        else:
            pass






if __name__ == "__main__":
    main()