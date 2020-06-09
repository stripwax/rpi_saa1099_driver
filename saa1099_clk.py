from RPi import GPIO
from time import sleep

DO_CLK = True

PIN_CLK = 4

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_CLK, GPIO.OUT, initial=GPIO.LOW)


def clk():
    GPIO.output(PIN_CLK, True)
    sleep(1/1600)
#    sleep(100/1e6)
    GPIO.output(PIN_CLK, False)
    sleep(1/1600)
#    sleep(100/1e6)

if __name__=='__main__':
    import signal
    import sys
    import random

    global clean_shutdown
    clean_shutdown = False

#    def signal_handler(sig, frame):
#        global clean_shutdown
#        if not clean_shutdown:
#            reset_sound()
#            GPIO.cleanup()
#            clean_shutdown = True
#        sys.exit(0)
#
#    signal.signal(signal.SIGINT, signal_handler)

    try:
        init()

        while(True):
#            sleep(0.01)
            clk()

    finally:
        GPIO.cleanup()
        clean_shutdown = True
