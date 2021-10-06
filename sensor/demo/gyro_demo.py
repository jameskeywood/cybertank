import board
import busio
import adafruit_fxos8700
import adafruit_fxas21002c
from time import sleep
from math import atan,sqrt
import numpy as np
from madgwickahrs import MadgwickAHRS

i2c = busio.I2C(board.SCL, board.SDA)
fxos = adafruit_fxos8700.FXOS8700(i2c)
fxas = adafruit_fxas21002c.FXAS21002C(i2c)

while True:
    print('Acceleration (m/s^2): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(*fxos.accelerometer))
    print('Magnometer (uTesla): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(*fxos.magnetometer))
    print('Gyroscope (radians/s): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(*fxas.gyroscope))
    sleep(2)
    x = fxos.accelerometer[0]/9.81
    y = fxos.accelerometer[1]/9.81
    z = fxos.accelerometer[2]/90oo
    pitch = atan(y/sqrt(x**2 + z**2))
    print(pitch)

heading = MadgwickAHRS()
while True:
    heading.update(fxos.accelerometer, fxos.magnetometer, fxas.gyroscope)
    ahrs = heading.quaternion.to_euler_angles()
    roll = ahrs[0]
    pitch = ahrs[1]
    yaw = ahrs[2]
    sleep(1)
