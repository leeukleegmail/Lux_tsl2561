from machine import Pin, I2C
import tsl2561

i2c = I2C(scl=Pin(5), sda=Pin(4))
lux = tsl2561.TSL2561(i2c=i2c)

while True:
    print(lux.read())
