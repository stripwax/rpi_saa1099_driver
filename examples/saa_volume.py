from RPi import GPIO
import time
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
    sound(28,2)
    sound(20,63)
    sound(16,255)
    sound(17,255)
    sound(18,255)
    sound(8,255)
    sound(9,255)
    sound(10,255)
    sound(11,255)
    sound(12,255)
    sound(13,255)
    sound(28,1)

    while(True):
        for i in range(16):
            for j in range(6):
                sound(j,i*17)
#            time.sleep(0.5)
            input('key')

