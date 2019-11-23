from logger import Logger
from send import Transceiver
from visualize import *
from alarm import *
import time

log = Logger()
message = Transceiver()
alarm = Alarm()

def main():
    while True:
        pi_data = message.receive()

        if (pi_data == 0x00):
            log.write("Normal operation, no fires detected.", "log.txt", False)
        elif (pi_data == 0x01):
            alarm.sound_alarm()
            log.write("Alert! Fire detected.", "log.txt", True)
        else:
            log.write("Error. Module not operational.", "log.txt", "Error")

    time.sleep(1)



if __name__ == "__main__":
    main()