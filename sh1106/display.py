from machine import Pin, I2C
import sh1106
from time import sleep_ms



i2c = I2C(0,scl=Pin(17), sda=Pin(16), freq=400000)
display = sh1106.SH1106_I2C(128, 64, i2c,None , 0x3c, 180)
display.sleep(False)
display.fill(0)
display.text('Ing. Armando', 1, 1, 1)
display.text ("Temperatura:", 0, 10, 1)
display.text ("Humedad:", 0, 20, 1)


display.show()
display.invert(0)
