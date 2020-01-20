import cv2
import numpy as np

image = cv2.imread('image.jpg')

size = image.size

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# red colour
low_red = np.array([0, 155, 84])
high_red = np.array([10, 255, 255])
red_mask = cv2.inRange(hsv_image, low_red, high_red)

# blue colour
low_blue = np.array([94, 80, 2])
high_blue = np.array([126, 255, 255])
blue_mask = cv2.inRange(hsv_image, low_blue, high_blue)

# green colour
low_green = np.array([25, 52, 72])
high_green = np.array([102, 255, 255])
green_mask = cv2.inRange(hsv_image, low_green, high_green)

# yellow colour
low_yellow = np.array([10, 155, 84])
high_yellow = np.array([20, 255, 255])
yellow_mask = cv2.inRange(hsv_image, low_yellow, high_yellow)

no_red = cv2.countNonZero(red_mask)
frac_red = np.divide(float(no_red), float(size))
percent_red = np.multiply(float(frac_red), 100)

no_blue = cv2.countNonZero(blue_mask)
frac_blue = np.divide(float(no_blue), float(size))
percent_blue = np.multiply(float(frac_blue), 100)

no_green = cv2.countNonZero(green_mask)
frac_green = np.divide(float(no_green), float(size))
percent_green = np.multiply(float(frac_green), 100)

no_yellow = cv2.countNonZero(yellow_mask)
frac_yellow = np.divide(float(no_yellow), float(size))
percent_yellow = np.multiply(float(frac_yellow), 100)

print('Red: ' + str(percent_red))
print('Blue: ' + str(percent_blue))
print('Green: ' + str(percent_green))
print('Yellow: ' + str(percent_yellow))
