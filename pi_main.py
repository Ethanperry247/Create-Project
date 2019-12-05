from logger import Logger
# from send import Transceiver
# from alarm import *
from light_alarm import *
from data import *
from irobot_test import *
from AudioTransceiver import *
import time


# LED alarm with pin 13.
# alarm = LEDAlarm(13)

# Transceiver to send data over to the master node.
sender = Radio("AAAA", "/dev/ttyUSB0")

# Sensor to detect flame.
sensor = FlameSensor(7)

#Starts up the robot.
robot = Robot("/dev/ttyUSB1")

def main():
    # Loop until closing.
    while True:
        if (sensor.flame_detected()):

            # Sends a "true" signal over to the master node.
            sender.write(b'A','BBBB')
            # Signals local alarm (LED Flash).
            # alarm.signal_alarm()
            time.sleep(1)
        else:
            # Affirms to the master node that no flame has been detected.
            sender.write(b'N', 'BBBB')
            time.sleep(1)
        # if (sender.receive_robot_code() is not None):
            # robot.run(sender.receive_robot_code())

        # if (sender.read() != b''):
            # robot.run(sender.read())


if __name__ == "__main__":
    main()
