# read_serial.py
# Serial reading functions

from serial import Serial

class SerialReader:
    """ Reads from the serial port """
    def __init__(self, port):
        self.serial = Serial(port, 9600)
        print("Serial port initialised on", port)

    def read_next_value(self):
        line = self.serial.readline().decode('ascii')
        print(line)
        return float(line)

    def close(self):
        self.serial.close()
