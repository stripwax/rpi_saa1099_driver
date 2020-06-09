from RPi import GPIO
from time import sleep
from random import randint
from saa1099_lib import sound, init, reset_sound


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

    init()
    reset_sound()
    sound(28,1)

    while(True):
#        sound(randint(0,31),randint(0,255))
        sound(randint(0,255),randint(0,255))
        sound(28,1)
        sound(31,1)
        sleep(0.01)
