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

mypin = 23
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
		
print(mypin)
GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering  
GPIO.setup(mypin, GPIO.IN)    # set GPIO25 as input (button)  
GPIO.setup(5, GPIO.OUT)  
# Define a threaded callback function to run in another thread when events are detected  
def my_callback(channel):  
    if GPIO.input(mypin):     # if port 25 == 1  
        print "Rising edge detected on ", mypin
	#GPIO.output(5, 1)
	db_write(1)	
    else:                  # if port 25 != 1  
        print "Falling edge detected on 5"
	#GPIO.output(5, 0)
	db_write(0)
  
# when a changing edge is detected on port 25, regardless of whatever   
# else is happening in the program, the function my_callback will be run  
GPIO.add_event_detect(mypin, GPIO.BOTH, callback=my_callback, bouncetime=1000)  
  
#raw_input("Press Enter when ready\n>")  
  
try:  
    print "When pressed, you'll see: Rising Edge detected on 25"  
    print "When released, you'll see: Falling Edge detected on 25"  
    while True:
    	pass
    #sleep(30)         # wait 30 seconds  
    print "Time's up. Finished!"  
  
finally:                   # this block will run no matter how the try block exits  
    GPIO.cleanup()         # clean up after yourself
