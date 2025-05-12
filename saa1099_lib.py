from RPi import GPIO
from time import sleep

DO_CLK = False
CLK_HZ = 8000000
#CLK_HZ = 4000
ticks = 0

PIN_a0 = 2
PIN_CS = 3
PIN_CLK = 4
PIN_WR = 14
PIN_d0 = 1
PIN_d1 = 7
PIN_d2 = 8
PIN_d3 = 25
PIN_d4 = 24
PIN_d5 = 23
PIN_d6 = 18
PIN_d7 = 15

def wait(ns):
#    sleep(1000*ns/1e9)
    sleep(ns/1e9)
#    sleep(ns/1000)
#    clk()
#    if DO_CLK:
#        clk()

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_a0, GPIO.OUT)
    GPIO.setup(PIN_CS, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(PIN_WR, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(PIN_d0, GPIO.OUT)
    GPIO.setup(PIN_d1, GPIO.OUT)
    GPIO.setup(PIN_d2, GPIO.OUT)
    GPIO.setup(PIN_d3, GPIO.OUT)
    GPIO.setup(PIN_d4, GPIO.OUT)
    GPIO.setup(PIN_d5, GPIO.OUT)
    GPIO.setup(PIN_d6, GPIO.OUT)
    GPIO.setup(PIN_d7, GPIO.OUT)
    if DO_CLK:
        GPIO.setup(PIN_CLK, GPIO.OUT, initial=GPIO.LOW)
        GPIO.output(PIN_CLK, 0)

    GPIO.output([PIN_a0, PIN_CS, PIN_WR, PIN_d0, PIN_d1, PIN_d2, PIN_d3, PIN_d4, PIN_d5, PIN_d6, PIN_d7],
                [0,1,1,0,0,0,0,0,0,0,0])


def set_clock(clock):
    if clock is None:
        # use external clock
        DO_CLK = False
        CLK_HZ = None
    else:
        DO_CLK = True
        CLK_HZ = clock
        ticks = 0


def set_reg(reg):
    '''Set the SAA1099 register'''
    write_a0(True)
    _write_cycle(reg)

def set_value(value):
    '''Send a value to SAA1099'''
    # see comments as for set_reg except a0 is False
    write_a0(False)
    _write_cycle(value)

def _write_cycle(data):
    '''complete the write cycle (assumes A0 already set)'''
    # t_ASC (time from A0 to CS low) is zero ns
    _set_CS(True) # active low, the _set_CS flips the sign for you
    # data must be valid at least 100 ns before WR is de-asserted
    # so we might as well do this as early as possible
    _set_data(data)
    # CS low to WR fall must be min 30 ns
    # A0 setup to WR fall must be min 50 ns
    wait(50)

    _set_WR(True) # active low, the _set_WR flips the sign for you

    # WR must be low for at least 100 ns
    wait(100)

    # deassert WR
    _set_WR(False)
    # minimum CS hold time after WR deasserted is 0 ns
    _set_CS(False)

    # A0 hold time and data bus hold time after WR deasserted
    # is min 0 ns, so we're done here
    # however, minimum bus cycle time for loading data into a register
    # (worst case) is 16 clocks.  So we could always just do that.
    for i in range(0,16):
        clk()


def write_a0(b):
    '''A0 active high'''
    GPIO.output(PIN_a0, b)


def _set_CS(b):
    '''CS active low'''
    GPIO.output(PIN_CS, not b)


def _set_WR(b):
    '''WR active low'''
    GPIO.output(PIN_WR, not b)


def _set_data(d):
    GPIO.output((PIN_d0, PIN_d1, PIN_d2, PIN_d3, PIN_d4, PIN_d5, PIN_d6, PIN_d7),
                bits(d))


def bits(d):
    return [d&(2**i)>0 for i in range(0,8)]


def sound(reg,val):
    set_reg(reg)
    set_value(val)


def reset_sound():
    sound(28,0)
    for i in range(0,29):
        sound(i,0)


def clk():
    if DO_CLK:
        if CLK_HZ == 0:
            global ticks
            # manual clock
            GPIO.output(PIN_CLK, True)
            input('tick %d'%(ticks))
            GPIO.output(PIN_CLK, False)
            input('tock %d'%(ticks))
            ticks += 1
        else:
            GPIO.output(PIN_CLK, True)
            sleep(0.5/CLK_HZ)
            GPIO.output(PIN_CLK, False)
            sleep(0.5/CLK_HZ)
    else:
        sleep(1/CLK_HZ)


