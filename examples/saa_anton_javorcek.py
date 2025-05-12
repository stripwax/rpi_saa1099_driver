from RPi import GPIO
import time
from random import randint
from saa1099_lib import sound, init, reset_sound, set_reg, set_value


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
    for v in range(0,16):
        print(f'Amplitude {v}')
        sound(2,v*17)
        for i in range(500):
            sound(24,0b10000010)
            #time.sleep(0.00025)
            sound(24,0b10010010)
            #time.sleep(0.00025)

