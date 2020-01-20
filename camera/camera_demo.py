#imports necesssary modules
from picamera import PiCamera
import time

#sets up camera variable
#sets the framerate of the preview to 60
camera = PiCamera(framerate = 60)

#rotates the camera preview by 180 degrees
#camera.rotation = 180

#starts camera preview
#sets fullscreen mode to false
#sets the window size
camera.start_preview(fullscreen = False, window = (0, 0, 500, 600))

#sleeps the program for 10 seconds
time.sleep(10)

#stops camera preview
camera.stop_preview()

#rotates the camera preview by 180 degrees
#camera.rotation = 180
