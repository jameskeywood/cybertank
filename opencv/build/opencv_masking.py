import cv2
import numpy as np

image = cv2.imread('image.jpg')
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

cv2.namedWindow('Red Mask',cv2.WINDOW_NORMAL)
cv2.resizeWindow('Red Mask', 600,600)
cv2.imshow("Red Mask", red_mask)
key = cv2.waitKey(0)

cv2.namedWindow('Blue Mask',cv2.WINDOW_NORMAL)
cv2.resizeWindow('Blue Mask', 600,600)
cv2.imshow("Blue Mask", blue_mask)
key = cv2.waitKey(0)

cv2.namedWindow('Green Mask',cv2.WINDOW_NORMAL)
cv2.resizeWindow('Green Mask', 600,600)
cv2.imshow("Green Mask", green_mask)
key = cv2.waitKey(0)

cv2.namedWindow('Yellow Mask',cv2.WINDOW_NORMAL)
cv2.resizeWindow('Yellow Mask', 600,600)
cv2.imshow("Yellow Mask", yellow_mask)
key = cv2.waitKey(0)

cv2.namedWindow('Original',cv2.WINDOW_NORMAL)
cv2.resizeWindow('Original', 600,600)
cv2.imshow("Original", image)
key = cv2.waitKey(0)
