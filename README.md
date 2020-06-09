# rpi_saa1099_driver
Driver for raspberry pi interface to SAA1099 sound chip

http://www.vgmpf.com/Wiki/images/1/19/SAA1099_-_Manual_-_1984.pdf

Before connecting raspberr\y pi to saa1099 board:
Use raspi-config->Advanced->Interfacing options to disable the following three items
 I2C
 SPI
 SERIAL CONSOLE

Pin mappings

| SAA PIN | RPI PIN (BCM) | RPI PIN (BOARD) |
|---------|---------------|-----------------|
|1  !WR   |GPIO 14 / TXD0 |  8              |
|2  !CS   |GPIO 3 / SCL1  |  5              |
|3  A0    |GPIO 2 / SDA1  |  3              |
|4  OUTR  |-              |                 |
|5  OUTL  |-              |                 |
|6  Iref  |-              |                 |
|7  !DTACK|nc             |                 |
|8  CLK   |GPIO 4 / GPCLK0|  7              |
|9  Vss   |-              |                 |
|10 D0    |GPIO 1 / ID_SC | 28              |
|11 D1    |GPIO 7 / SPICE1| 26              |
|12 D2    |GPIO 8 / SPICE0| 24              |
|13 D3    |GPIO 25        | 22              |
|14 D4    |GPIO 24        | 18              |
|15 D5    |GPIO 23        | 16              |
|16 D6    |GPIO 18        | 12              |
|17 D7    |GPIO 15 / RXD0 | 19              |
|18 Vdd   |-              |                 |
 
