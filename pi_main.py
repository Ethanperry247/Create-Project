from logger import Logger
from send import Transceiver
from visualize import *
from alarm import *
from light_alarm import *
from data import *

# LED alarm with pin 13.
alarm = LEDAlarm(13)

# Transceiver to send data over to the master node.
sender = Transceiver("/dev/ttyUSB0", 125000, "0013A200419B5611", 1)

# Sensor to detect flame.
sensor = FlameSensor(7)

def main():

    # Loop until closing.
    while True:
        if (sensor.flame_detected()):

            # Sends a "true" signal over to the master node.
            sender.send([0x01, sender.get_id_number()])
            # Signals local alarm (LED Flash).
            alarm.signal_alarm()
        else:
            # Affirms to the master node that no flame has been detected.
            sender.send([0x00, sender.get_id_number()])


if __name__ == "__main__":
    main()