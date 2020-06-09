import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import time

GPIO.setup(4, GPIO.OUT)

d = 1

while True:
    GPIO.output(4, False)
    input('tick %d'%(d))

    GPIO.output(4, True)
    input('tock %d'%(d))

    d += 1
    

