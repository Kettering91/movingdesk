# Project: MovingDesk
# Version: 1.0
# Date: 2022_05_19
# Devel: M. Gebing


from machine import Pin, SPI

#import chardet
import os
import sys
import time
import logging
import spidev as SPI1
from lib import LCD_1inch28
from PIL import Image,ImageDraw,ImageFont


""" just test program
led = Pin(25, Pin.OUT)
while True:
    led(1)
    time.sleep(1)
    led(0)
    time.sleep(1)
"""

# Config Pin
DIN = 11
CLK = 10
CS = 9
DC = 8
RST = 12
BL = 13
bus = 0
device = 0
# configure SPI
spi = SPI(1, baudrate=40000000, sck=Pin(10),mosi=Pin(11))

disp = LCD_1inch28.LCD_1inch28(spi= SPI1.SpiDev(bus,device), spi_freq=40000000, rst=RST, dc=DC, bl=BL)
