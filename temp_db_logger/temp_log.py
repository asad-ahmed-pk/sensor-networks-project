# temp_log.py

import db_connect
import time
import sys
import signal
import serial

from read_serial import SerialReader

def log_temp_db(temp, cursor):
    insert = "INSERT INTO temperature(temp) VALUES(%s)"
    cursor.execute(insert, (temp,))
    return cursor.lastrowid

def main():

    # init

    # connect to mysql database
    db_link = db_connect.connect_db()
    cursor = db_link.cursor(buffered=True)

    # init serial reader
    serial_reader = SerialReader("/dev/tty.usbmodem14101")

    # main running loop
    while (True):

        try:
            # read next temp value from reader and log to db
            temp_value = serial_reader.read_next_value()
            last_id = log_temp_db(temp_value, cursor)
            db_link.commit()
            print("Inserted record with id:", last_id)

            time.sleep(1.0)
        except KeyboardInterrupt:
            serial_reader.close()
            print("Program Stopped")
            sys.exit(0)

main()
