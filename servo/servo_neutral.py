import RPi.GPIO as GPIO
import time

servoPIN = 6
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(7.5) # Initialization
p.ChangeDutyCycle(2.5)
GPIO.cleanup()
