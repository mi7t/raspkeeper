import RPi.GPIO as GPIO
from datetime import date, datetime, timedelta

GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN)
GPIO.add_event_detect(6, GPIO.RISING)  # add rising edge detection on a channel
#do_something()
if GPIO.event_detected(6):
    print('Button pressed')
