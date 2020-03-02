from sense_hat import SenseHat
import time
 
sense = SenseHat()
 
while True:
    orientation = sense.get_orientation()
    p=round(orientation["pitch"])
    r=round(orientation["roll"])
    y=round(orientation["yaw"])
    print("p: {}, r: {}, y: {}".format(p, r, y))
    time.sleep(0.1)