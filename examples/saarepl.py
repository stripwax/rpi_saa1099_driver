import signal
import sys
import random
from RPi import GPIO
from time import sleep
from saa1099_lib import init, sound, reset_sound, set_clock, set_manual_clock, set_reg, set_value, clk
import saa1099_lib
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--manual_clock', action='store_true', help='If set, clocking is manual')
    parser.add_argument('--clock_rate', type=int, help='Clock rate in Hz.  Ignored if manual_clock is True. Note, this just sets timing, and doesn\'t generate the clock signal', default=8000000)
    args = parser.parse_args()

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
    set_clock(args.clock_rate)
    set_manual_clock(args.manual_clock)

    while(True):
        regval = input('reg,val (or just reg, or just ,val):  (or just enter for a clock tick if manual clock)')
        try:
            inputs = regval.split(',')
            if not inputs or (len(inputs)==1 and not len(inputs[0].strip())):
                if args.manual_clock:
                    print(f'tick ... tock ... {saa1099_lib.ticks}')
                    clk()
                else:
                    print('ignoring empty input')
            elif len(inputs)==2 and inputs[1]:
                reg, value = inputs
                if reg:
                    if reg=="c" and args.manual_clock:
                       print(f'{value} ticks:')
                       for i in range(int(value)):
                           clk()
                    else:
                        print(f'{reg} => {value}')
                        sound(int(reg), int(value))
                else:
                    print(f'=> {value}')
                    set_value(int(value))
            elif len(inputs)==1 or not inputs[1]:
                reg = int(inputs[0])
                print(f'{reg} =>')
                set_reg(reg)
            else:
                print('ignoring input {inputs}')
        except Exception as e:
            print('Ignoring input that couldn\'t be parsed as integers\n'+e)


if __name__=='__main__':
    main()
