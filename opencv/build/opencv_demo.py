import cv2
import numpy as np

image = cv2.imread('image.jpg')
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# red colour
low_red = np.array([161, 155, 84])
high_red = np.array([179, 255, 255])
mask = cv2.inRange(hsv_image, low_red, high_red)

cv2.namedWindow('Red Mask',cv2.WINDOW_NORMAL)
cv2.resizeWindow('Red Mask', 600,600)

cv2.imshow("Red Mask", mask)

key = cv2.waitKey(0)

cv2.namedWindow('Original',cv2.WINDOW_NORMAL)
cv2.resizeWindow('Original', 600,600)

cv2.imshow("Original", image)

key = cv2.waitKey(0)

