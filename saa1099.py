from RPi import GPIO
from time import sleep
from saa1099_lib import sound, reset_sound, init


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
        sleep(1)
#        input('after init, wait for key here')
        reset_sound()
#        input('after reset, wait for key here, then enable')
        for i in range(0,32):
            sound(i,255)
#        input('after all reg enabled, wait for key here')
        sound(28,1)
        sound(28,2)
#        sound(28,2)
#        sound(0,2*16)
#        sound(2,10)
        sound(0,255)
#       sound(1,255)
#       sound(2,255)
#        sound(3,15)
        sound(20,63)
#        sound(20,31)
#        sound(21,31)

        sound(8,255)
#        sound(9,128)
#        sound(10,64)
#        sound(16,3+3*16)
        sound(16,7+7*16)
#        sound(17,3)
	#        sound(24,14+128+32)
#        sound(24,14+128)
#       sound(24,2+128+32)
#        set_reg(24)
#        sound(24,130)
#        sound(28,1)
 #       input('wait for key here, then enable')
        sleep(10)
        sound(28,1)
#        input('wait for key here, then disable')
        sleep(10)
        sound(28,0)
#        input('wait for key here, then enable again and do pitch ramp')
        sleep(10)
        sound(28,1)

        for i in range(0,255):
            sound(8,i)
            sleep(0.2)

#        while(True):
#            sleep(0.1)

#            clk()

#        input('Press any key...')
#        sound(24,6+128+32)

#        i = 0
#        while(True):
#            sound(2,255)
#            input('Press any key...')
#            sound(2,0)
#            input('Press any key...')
#            sound(24,130)
#            input('Press any key...')

#            sound(24,0)
#            sleep(0.0223)
#            sleep(0.2)
#            sound(24,2+128+32)
#            sound(28,3)
#            sound(28,1)
#            sound(24,6+128+32)
#            sound(28,1)
#            set_reg(24)
#            sound(28,3)
#            sound(28,1)
#            input('Press any key...')

 #       while(True):
 #           for i in range(0,16):
 #               set_reg(24)
 #               input('Press any key...')
 #               sleep(0.1)

        while(True):
            sleep(0.5)
            sound(16, random.randint(0,7))
            sound(8, random.randint(0,255))

    finally:
        reset_sound()
        GPIO.cleanup()
        clean_shutdown = True
