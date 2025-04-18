import adafruit_ds3231
import time
import busio
import board

"""
day of year and summertime (last two parameters in struct_time) are NOT implemented by adafruit_ds3231. ignore!
"""

i2c = busio.I2C(scl=board.GP1, sda=board.GP0)
rtc = adafruit_ds3231.DS3231(i2c)

def set_dt(Y, M, D, h, m, s):
    rtc.datetime = time.struct_time((Y, M, D, h, m, s, -1, -1, -1)) # set datetime.
    
def get_struct_time():
    return rtc.datetime

def set_dt_input():
    Y = int(input("Input Year in YYYY: "))
    M = int(input("Input Month in MM: "))
    D = int(input("Input Year in DD: "))
    h = int(input("Input Hour in hh: "))
    m = int(input("Input Minutes in mm: "))
    s = int(input("Input Seconds in ss: "))
    
    set_dt(Y, M, D, h, m, s)
    print("Done!")

