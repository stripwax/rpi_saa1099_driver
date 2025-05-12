from RPi import GPIO
from time import sleep
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
    sound(2,255)
    sound(20,4)
    sound(24,0b10101110)
    for i in range(0,16):
        print(i, '/15')
        input('press a key')
        set_reg(24)
    for i in range(0,16):
        print(i, '/15')
        input('press a key')
        set_reg(24)

    while(True):
        set_value(0b10111110)
        input('silence (press a key)')
        set_value(0b10101110)
        input('not silence (press a key)')
