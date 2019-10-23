# xbee_read.py
# XBee reader module

from xbee import XBee


class XBeeReader():
    """ Reads temp stream from the XBee reciever """
    def __init__(self, port_number, baud_rate=9600):
        self.xbee = XBee(port_number, baud_rate)
        self.xbee.open()
        print("XBee reader initialised")

    def read_next_temp(self):
        """ Return the next temp value in the stream """
        msg = self.xbee.read_data()

        # todo: parse message
        print(msg)
        return 0.0

    def close(self):
        self.xbee.close()

class FakeXBeeReader():
    def __init__(self, port_number, baud_rate=9600):
        self.temp = 0.0
        print("XBee reader initialised")

    def read_next_temp(self):
        """ Return the next temp value in the stream """
        self.temp += 0.1
        return self.temp

    def close(self):
        print("Connection to XBee closed")
        