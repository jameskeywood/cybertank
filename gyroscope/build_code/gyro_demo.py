import board
import busio
import adafruit_fxos8700
import adafruit_fxas21002c
from time import sleep

i2c = busio.I2C(board.SCL, board.SDA)
fxos = adafruit_fxos8700.FXOS8700(i2c)
fxas = adafruit_fxas21002c.FXAS21002C(i2c)

while True:
    print('Acceleration (m/s^2): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(*fxos.accelerometer))
    print('Magnometer (uTesla): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(*fxos.magnetometer))
    print('Gyroscope (radians/s): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(*fxas.gyroscope))
    sleep(2)