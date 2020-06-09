import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import time

GPIO.setup(4, GPIO.OUT)

while True:
    GPIO.output(4, False)
    time.sleep(0.01)
    GPIO.output(4, True)
    time.sleep(0.01)
    

