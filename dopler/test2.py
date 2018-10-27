import RPi.GPIO as GPIO
from datetime import date, datetime, timedelta
import mysql.connector

config = {
  'user': 'mist',
  'password': 'mist',
  'host': '127.0.0.1',
  'database': 'db1',
  'raise_on_warnings': True,
}


def db_write(str):
	cnx = mysql.connector.connect(**config)
	cursor = cnx.cursor()
	#action_date = datetime.now().date() + timedelta(days=1)
	action_date = datetime.now()
	cursor = cnx.cursor()
	add_action = ("INSERT INTO stage1 (element, value_bin, change_date) VALUES (%s, %s, %s)")
	data_action = ('Button1',str, action_date)
	cursor.execute(add_action, data_action)
	cnx.commit()
	cursor.close()
	cnx.close()
	return

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
print GPIO.input(14)
db_write(GPIO.input(14)) 
