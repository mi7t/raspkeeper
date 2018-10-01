import RPi.GPIO as GPIO
from time import sleep
posledny = 0
aktualny = 0
mypin = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(mypin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
while True:
 aktualny = GPIO.input(mypin)
 #print GPIO.input(mypin)
 if aktualny != posledny:
  print "Aktualny :",aktualny
  #print "Posledny :",posledny
 posledny = aktualny
 sleep(1)
