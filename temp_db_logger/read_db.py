# read_db.py
# Reads the last temperature value from the database
# For Jerry :D

import db_connect

def get_last_temp_record():
	db_link = db_connect.connect_db()
	cursor = db_link.cursor(buffered=True)

	sql = "SELECT temp,creation_date FROM temperature ORDER BY creation_date DESC LIMIT 1"
	cursor.execute(sql)

	temp = 0.0
	time = None
	for (temp, creation_date) in cursor:
		temp = temp
		time = creation_date
		break
	cursor.close()
	return temp, time


# example usage
#temp, time = get_last_temp_record()
#print(temp, time)