import RPi.GPIO as GPIO
from datetime import date, datetime, timedelta
import mysql.connector

from time import sleep

config = {
  'user': 'mist',
  'password': 'mist',
  'host': '127.0.0.1',
  'database': 'db1',
  'raise_on_warnings': True,
}

posledny = 0
aktualny = 0
mypin = 23
i = 0
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
GPIO.setup(mypin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
while True:
 aktualny = GPIO.input(mypin)
 #print GPIO.input(mypin)
 if aktualny != posledny:
  print "Aktualny :",aktualny
  #print "Posledny :",posledny
  print "Pocet :",i
  db_write(aktualny)
  i = 0 
 else:
  i = i+1
 posledny = aktualny
 sleep(1)
