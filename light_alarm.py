import RPi.GPIO as GPIO
import time

class LEDAlarm():

    channel = 0

    def __init__(self, chan=27):
        channel = chan
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(channel, GPIO.OUT)


    def signal_alarm(self):
        GPIO.output(channel, 1)
        time.sleep(0.2)