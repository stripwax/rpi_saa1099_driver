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
    sound(24,0b10101100)
    for i in range(0,33):
        print(i, '/32')
        input('press a key')
        set_reg(24)

    sound(20,4)
    sound(24,0b10101100)
    for i in range(0,33):
        print(i, '/32')
        input('press a key')
        if i==10:
            set_value(0b10100010)
        if i==10:
            set_value(0b10100000)
        if i==10:
            set_value(0b10100110)
        if i==15:
            set_value(0b10100000)
        if i==15:
            set_value(0b10100010)
        if i==16:
            set_value(0b10100001)
        set_reg(24)




