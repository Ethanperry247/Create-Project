# import RPi.GPIO as GPIO
import time

# Sensor superclass.
class Sensor:

    channel = 0

    def __init__(self, chan=27):
        channel = chan
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(channel, GPIO.IN)

# Flame, Gas, and Carbon Monoxide (and other) Sensors.
class FlameSensor(Sensor):

    def __init__(self):
        super().__init__()
    
    def flame_detected(self):
        if (GPIO.input(Sensor.channel)):
            return "FLAME DETECTED"

class GasSensor(Sensor):

    def __init__(self):
        super().__init__()
    
    pass

class COSensor(Sensor):

    def __init__(self):
        super().__init__()

    pass

class TempSensor(Sensor):

    def __init__(self):
        super().__init__()

    pass

class HumiditySensor(Sensor):

    def __init__(self):
        super().__init__()

    pass


