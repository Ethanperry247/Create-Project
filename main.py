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
            time.sleep(0.5)
        elif (pi_data == b'A'):
            alarm.sound_alarm()
            log.write("Alert! Fire detected.", file, id_number, "True")
        else:
            log.write("Error. Module not operational.", file, id_number, "Error")
            time.sleep(0.5)

        robot_state = robot.run()

        if (robot_state is not None):
            print (robot_state)
            if (robot_state == 2):
                radio.write(b'W', "AAAA")
            elif (robot_state == 3):
                radio.write(b'S', "AAAA")
            elif (robot_state == 4):
                radio.write(b'A', "AAAA")
            elif (robot_state == 5):
                radio.write(b'D', "AAAA")
            else:
                radio.write(b'F', "AAAA")
                print ("Incorrect Key Command")
        else:
            radio.write(b'F',"AAAA")
            print ("called")

    time.sleep(1)



if __name__ == "__main__":
    main()
