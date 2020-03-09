import pygame
import time

pygame.init()
pygame.joystick.init()

while True:
    if pygame.joystick.get_count() == 1:
        print("Joystick Connected")
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        break

while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        # up and down movement
        upDown = -joystick.get_axis(1)
        if upDown > 0:
            print("up")                     
        elif upDown < 0:
            print("down")

        upDown = -joystick.get_axis(4)
        if upDown > 0:
            print("up")          
        elif upDown < 0:
            print("down")

        # servo left right
        leftRight = -joystick.get_axis(0)
        if leftRight > 0:
            print("left")              
        elif leftRight < 0:
            print("right")
            
        leftRight = -joystick.get_axis(3)
        if leftRight > 0:
            print("left")              
        elif leftRight < 0:
            print("right")

