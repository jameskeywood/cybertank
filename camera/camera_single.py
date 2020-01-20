#imports
from io import BytesIO
from picamera import PiCamera

#sets the camera variable
camera = PiCamera()

#creates a file called "image.jpg"
my_file = open("image.jpg", "wb")

#captures this image
camera.capture(my_file)

#closes the file
my_file.close()
