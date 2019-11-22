# import RPi.GPIO as GPIO
import time

# Sensor superclass.
class Sensor:

    channel = 0

    def __init__(self, chan=27):
        channel = chan
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(channel, GPIO.IN)

class FlameSensor(Sensor):
    
    def flame_detected(self):
        if (GPIO.input(Sensor.channel)):
            return "FLAME DETECTED"

class GasSensor(Sensor):
    pass

class COSensor(Sensor):
    pass

