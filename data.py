# import RPi.GPIO as GPIO
import time

class FlameSensor():

    channel = 0

    def __init__(self, chan=27):
        channel = chan
        GPIO.setup(channel, GPIO.IN)
    
    def flame_detected(self):
        pass
