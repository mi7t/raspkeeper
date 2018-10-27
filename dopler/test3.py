import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.add_event_detect(channel, GPIO.RISING, callback=my_callback)
