# rpi_saa1099_driver
Driver for raspberry pi interface to SAA1099 sound chip

http://www.vgmpf.com/Wiki/images/1/19/SAA1099_-_Manual_-_1984.pdf

Before connecting raspberry pi to saa1099 board:
Use raspi-config->Advanced->Interfacing options to disable the following three items
 I2C
 SPI
 SERIAL CONSOLE

Pin mappings

SAA PIN -> RPI PIN (BCM) -> RPI PIN (BOARD)
1  !WR     14               8
2  !CS     3                5
3  A0      2                3
4  OUTR    -
5  OUTL    -
6  Iref    -
7  !DTACK  nc
8  CLK     4                7
9  Vss     -

10 D0      1                28
11 D1      7                26 
12 D2      8                24
13 D3      25               22
14 D4      24               18
15 D5      23               16
16 D6      18               12
17 D7      15               19
18 Vdd     -
