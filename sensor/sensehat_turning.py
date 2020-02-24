from sense_hat import SenseHat
import time

sense = SenseHat()
orientation = sense.get_orientation()
yaw = round(orientation["yaw"])

while True:
    # measures values
    orientation = sense.get_orientation()
    prev_yaw = yaw
    yaw = round(orientation["yaw"])
    change = prev_yaw - yaw
    # prints values
    print("yaw: {}, change: {}".format(yaw, change))
    time.sleep(0.1)