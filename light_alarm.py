import RPi.GPIO as GPIO
import time

class LEDAlarm():

    def __init__(self, chan=13):
        self.channel = chan
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(channel, GPIO.OUT)


    def signal_alarm(self):
        GPIO.output(self.channel, 1)
        time.sleep(0.2)