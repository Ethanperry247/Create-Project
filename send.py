from digi.xbee.devices import *
from digi.xbee.util import *
from digi.xbee.exception import *

class Transceiver:

    def __init__(self, port, local_baud, remote_address, id_number):
        self.id_number = id_number;
        self.local_xbee = Raw802Device(port, local_baud)
        self.remote_device = RemoteXBeeDevice(local_xbee, XBee64BitAddress.from_hex_string
                                                    (remote_address))
    
    def send(self, data):
        local_xbee.open()
        try:
            local_xbee.send_data(remote_device, self.data)

        except:
            print (local_xbee.log)
        local_xbee.close()

    def receive(self):
        local_xbee.open()
        while True:
            xbee_message = local_xbee.read_data()
            if xbee_message:
                return xbee_message()
        local_xbee.close()
        
    def get_id_number(self):
        return self.id_number
