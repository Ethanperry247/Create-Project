from logger import Logger
from send import Transceiver
# from visualize import *
from alarm import *
import time
from irobot_test import *
from AudioTransceiver import *

# Creates a logger object to read, write, etc.
log = Logger()

# Creates a transceiver so that data may be received from the nodes.
radio = Radio("BBBB", "COM7")

# Prepares an alarm to be sounded if need be.
alarm = Alarm()

robot = RobotMessenger()

def main():

    file = "./CSCI 101/Create_Project/Create_Project/Visualizer/Viz/log.txt"


    # Clears any previously created file.
    log.erase(file)

    while True:
        # To be filled with message.receive().
        # pi_data = message.receive()[0]
        # id_number = message.receive()[1]
        id_number = 1
        pi_data = radio.read()
        print ("Running. Data Received:", pi_data)
        # pi_data = 0x00

        if (pi_data == b'N'):
            log.write("Normal operation, no fires detected.", file, id_number, "False")
            time.sleep(1)
        elif (pi_data == b'A'):
            alarm.sound_alarm()
            log.write("Alert! Fire detected.", file, id_number, "True")
            print ("A")
        else:
            log.write("Error. Module not operational.", file, id_number, "Error")
            time.sleep(1)

        # message.send(robot.run())

    time.sleep(1)



if __name__ == "__main__":
    main()
