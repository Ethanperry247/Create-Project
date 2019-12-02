from AudioTransceiver import *

radio = Radio()

radio.write(b'hello', "AAAA")

while True:
    radio.read()
    print(radio.read())