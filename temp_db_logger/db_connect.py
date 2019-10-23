# db_connect.py
# Python Database Connection Module

import mysql.connector

def connect_db():
    config = {
    'user': 'user06',
    'password': 'user06',
    'host': '10.50.202.242',
    'database': 'user06',
    'raise_on_warnings': True,
    }

    link = mysql.connector.connect(**config)
    return link
