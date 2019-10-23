# db_connect.py
# Python Database Connection Module

import mysql.connector

def connect_db():
    config = {
    'user': 'root',
    'password': '61f710c6',
    'host': '127.0.0.1',
    'database': 'sensor_network_db',
    'raise_on_warnings': True,
    }

    link = mysql.connector.connect(**config)
    return link
