import signal
import sys
import random
from RPi import GPIO
from time import sleep
from saa1099_lib import init, sound, reset_sound, set_clock, set_manual_clock, set_reg, set_value, clk
import saa1099_lib
import argparse
import time


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

    timestamp = 0  # basis 44.1kHz outputs
    time_start = time.time()

    for line in sys.stdin:
        print(f'@{saa1099_lib.ticks}:\t', end="")
        line = line.strip()
        if not line:
            continue
        try:
            if line.startswith('#'):
                print(line)
                continue

            splits = line.split(' ', 2)
            t, reg = splits[0], splits[1]
            if len(splits)==3:
                rest = splits[2]
            else:
                rest = ""

            t = int(t)
            time_t = time_start + t / 44100
            reg = int(reg)
            val = None
            clocks = None
            rest = rest.strip()
            if rest and not rest.startswith('#'):
                splits = rest.split(' ', 1)
                val = int(splits[0])
                rest = ""
                if len(splits) == 2:
                    rest = splits[1].strip()
                if rest and not rest.startswith('#'):
                    splits = rest.split(' ', 1)
                    clocks = int(splits[0])
                    rest = ""
                    if len(splits) == 2:
                        rest = splits[1].strip()

            if rest and len(rest) and not rest.startswith('#'):
                raise(ValueError('Too many fields, expected \# comment'))

            sleep = time_t - time.time()
            if sleep > 0:
                print(f'sleep {sleep}')
                time.sleep(sleep)

            if val is None or val == -1:
                print(f'{reg} =>')
                set_reg(reg)
            else:
                # we assume input is well-formed and reg is unchanged i.e. reg is correct even though we only send value
                print(f'{reg} => {val}')
                set_value(val)

            if clocks is not None:
                print(f'+ {clocks} ticks')
                for i in range(clocks): clk()

            if rest:
                print(rest)

        except Exception as e:
            print(f'Bad input {line}', e)


if __name__=='__main__':
    main()
