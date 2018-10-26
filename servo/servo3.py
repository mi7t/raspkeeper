import RPi.GPIO as GPIO
import time

servoPIN = 6
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(7.5) # Initialization
p.ChangeDutyCycle(6.5)
time.sleep(0.1)
p.ChangeDutyCycle(12.5)
time.sleep(0.1)
p.ChangeDutyCycle(7.5)
p.stop()
GPIO.cleanup()
