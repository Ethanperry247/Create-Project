from digi.xbee.devices import *
from digi.xbee.util import *
from digi.xbee.exception import *

xbee = Raw802Device('COM7', 250000)

remote_device = RemoteXBeeDevice(xbee, XBee64BitAddress.from_hex_string("0013A200419B5611"))

print (xbee.get_64bit_addr)