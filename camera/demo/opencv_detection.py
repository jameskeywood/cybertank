# imports
import cv2
import numpy as np
from io import BytesIO
from picamera import PiCamera

try:
    
    while True:

        # image capture
        camera = PiCamera()
        my_file = open("image.jpg", "wb")
        camera.capture(my_file)
        my_file.close()
        camera.close()
        
        # image variables
        image = cv2.imread('image.jpg')
        size = image.size
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # red colour boundaries
        low_red = np.array([0, 155, 84])
        high_red = np.array([10, 255, 255])
        red_mask = cv2.inRange(hsv_image, low_red, high_red)

        # blue colour boundaries
        low_blue = np.array([94, 80, 2])
        high_blue = np.array([126, 255, 255])
        blue_mask = cv2.inRange(hsv_image, low_blue, high_blue)

        # green colour boundaries
        low_green = np.array([25, 52, 72])
        high_green = np.array([102, 255, 255])
        green_mask = cv2.inRange(hsv_image, low_green, high_green)

        # yellow colour boundaries
        low_yellow = np.array([10, 155, 84])
        high_yellow = np.array([20, 255, 255])
        yellow_mask = cv2.inRange(hsv_image, low_yellow, high_yellow)

        # red colour percentage
        no_red = cv2.countNonZero(red_mask)
        frac_red = np.divide(float(no_red), float(size))
        percent_red = np.multiply(float(frac_red), 100)

        # blue colour percentage
        no_blue = cv2.countNonZero(blue_mask)
        frac_blue = np.divide(float(no_blue), float(size))
        percent_blue = np.multiply(float(frac_blue), 100)

        # green colour percentage
        no_green = cv2.countNonZero(green_mask)
        frac_green = np.divide(float(no_green), float(size))
        percent_green = np.multiply(float(frac_green), 100)

        # yellow colour percentage
        no_yellow = cv2.countNonZero(yellow_mask)
        frac_yellow = np.divide(float(no_yellow), float(size))
        percent_yellow = np.multiply(float(frac_yellow), 100)

        # print colour percentages
        print('\nRed: ' + str(percent_red))
        print('Blue: ' + str(percent_blue))
        print('Green: ' + str(percent_green))
        print('Yellow: ' + str(percent_yellow))

        # print target colour
        target_colour = 'unassigned'
        
        if percent_red > percent_blue and percent_red > percent_green and percent_red > percent_yellow:
            target_colour ='Red'
        elif percent_blue > percent_red and percent_blue > percent_green and percent_blue > percent_yellow:
            target_colour = 'Blue'
        elif percent_green > percent_red and percent_green > percent_blue and percent_green > percent_yellow:
            target_colour = 'Green'
        elif percent_yellow > percent_red and percent_yellow > percent_blue and percent_yellow > percent_green:
            target_colour = 'Yellow'
        else:
            target_colour = 'unnassinged'

        print('Target Colour: ' + target_colour)
        
except KeyboardInterrupt:
    
    print("\nProgram Interrupted")
