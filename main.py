from logger import Logger
from send import Transceiver
# from visualize import *
from alarm import *
import time

# Creates a logger object to read, write, etc.
log = Logger()

# Creates a transceiver so that data may be received from the nodes.
# message = Transceiver()

# Prepares an alarm to be sounded if need be.
alarm = Alarm()

def main():

    file = "./CSCI 101/Create_Project/Create_Project/Visualizer/Viz/log.txt"


    # Clears any previously created file.
    log.erase(file)

    temp = 0

    while True:
        # To be filled with message.receive().
        pi_data = 0x00

        temp+=1

        if (pi_data == 0x00 and temp < 15):
            log.write("Normal operation, no fires detected.", file, "False")
            time.sleep(1)
        elif (pi_data == 0x01 or temp >= 15):
            alarm.sound_alarm()
            log.write("Alert! Fire detected.", file, "True")
        else:
            log.write("Error. Module not operational.", file, "Error")
            time.sleep(1)

    time.sleep(1)



if __name__ == "__main__":
    main()