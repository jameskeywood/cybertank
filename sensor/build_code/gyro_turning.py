# program prints turning direction
import board
import busio
import adafruit_fxos8700
import adafruit_fxas21002c
import time

# assign variables
mag_x = 0

# initialize I2C bus and devices
i2c = busio.I2C(board.SCL, board.SDA)
fxos = adafruit_fxos8700.FXOS8700(i2c)
fxas = adafruit_fxas21002c.FXAS21002C(i2c)
 
# main loop reads values and prints them out
while True:
    # read acceleration, magnetometer and gyroscope
    prev_mag_x = mag_x
    mag_x, mag_y, mag_z = fxos.magnetometer
    difference = mag_x - prev_mag_x
    # print x values
    if mag_x > prev_mag_x:
        print("Left: " + str(difference))
    elif mag_x < prev_mag_x:
        print("Right: " + str(difference))
    else:
        print("None")
    # second time delay
    time.sleep(1)