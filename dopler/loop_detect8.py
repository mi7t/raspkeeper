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
outpin = 5
i = 0
odloz_ini = 5
odloz = odloz_ini
def todayAt (hr, min=0, sec=0, micros=0):
   now = datetime.now()
   return now.replace(hour=hr, minute=min, second=sec, microsecond=micros)    

def db_write(str,cnt):
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        #action_date = datetime.now().date() + timedelta(days=1)
        action_date = datetime.now()
        cursor = cnx.cursor()
        add_action = ("INSERT INTO stage1 (element, value_bin, counter, change_date) VALUES (%s, %s, %s, %s)")
        data_action = ('Button1',str, cnt, action_date)
        cursor.execute(add_action, data_action)
        cnx.commit()
        cursor.close()
        cnx.close()
        return
        
# Usage demo2:
timeNow = datetime.now()
if (timeNow < todayAt (17)) and (timeNow > todayAt (6)):
   svietim = 0
else :
   svietim = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(mypin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(outpin, GPIO.OUT)           # set GPIO24 as an output  
while True:
 aktualny = GPIO.input(mypin)
 #print GPIO.input(mypin)
 if aktualny != posledny:
  print "Aktualny, pocet povodny :",aktualny, i
  #print "Posledny :",posledny
  #print "Pocet :",i
  db_write(aktualny,i)
  i = 0 
  if aktualny == 1:
   GPIO.output(outpin, svietim) 
   odloz = odloz_ini 
 else:
  i = i+1
  if aktualny == 0:
   odloz = odloz -1
   if odloz < 1:
    print "Vypinam",posledny
    GPIO.output(outpin, 0)
   else:
     print "Cakam",odloz
 posledny = aktualny
 sleep(1)
