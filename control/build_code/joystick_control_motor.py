import UltraBorg
import pygame
import time

UB = UltraBorg.UltraBorg()
UB.Init()
pygame.init()
pygame.joystick.init()

while True:
    if pygame.joystick.get_count() ==1:
        print("Joytstick Connected")
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        break
    else:
        print("No Joystick Connected :(")
        break
