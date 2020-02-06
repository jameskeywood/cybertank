# program prints acceleration, magnetometer and gyroscope values every second
import time
import board
import busio
import adafruit_fxos8700
import adafruit_fxas21002c

# initialize I2C bus and devices
i2c = busio.I2C(board.SCL, board.SDA)
fxos = adafruit_fxos8700.FXOS8700(i2c)
fxas = adafruit_fxas21002c.FXAS21002C(i2c)
 
# main loop reads values and prints them out
while True:
    # read acceleration, magnetometer and gyroscope
    accel_x, accel_y, accel_z = fxos.accelerometer
    mag_x, mag_y, mag_z = fxos.magnetometer
    gyro_x, gyro_y, gyro_z = fxas.gyroscope
    # print values.
    print('Acceleration (m/s^2): ({0:0.3f}, {1:0.3f}, {2:0.3f})'.format(accel_x, accel_y, accel_z))
    print('Magnetometer (uTesla): ({0:0.3f}, {1:0.3f}, {2:0.3f})'.format(mag_x, mag_y, mag_z))
    print('Gyroscope (radians/s): ({0:0.3f}, {1:0.3f}, {2:0.3f})'.format(gyro_x, gyro_y, gyro_z))
    # delay for a second.
    time.sleep(1.0)