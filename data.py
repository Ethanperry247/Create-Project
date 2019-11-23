# import RPi.GPIO as GPIO
import time

# Flame, Gas, and Carbon Monoxide (and other) Sensors.
class FlameSensor():

    def __init__(self, channel):
        self.channel = channel
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(channel, GPIO.IN)
    
    def flame_detected(self):
        if (GPIO.input(self.channel)):
            print ("FLAME DETECTED")
            return True
        else:
            return False

    def get_channel(self):
        return self.channel
