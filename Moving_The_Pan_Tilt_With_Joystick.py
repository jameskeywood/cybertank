import UltraBorg
import pygame
import time

UB = UltraBorg.UltraBorg()
UB.Init()
pygame.init()
pygame.joystick.init()
move_to = 0
while True:
    if pygame.joystick.get_count() ==1:
        print("Joytstick Connected")
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        break

while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
        upDown = -joystick.get_axis(True)
        pos = UB.GetDistance3()
        #servo up down
        if upDown > 0:
            print("UP")
           
            if move_to < 0.9:
                move_to += 0.05
            UB.SetServoPosition4(move_to)
            pos = UB.GetDistance3()
                
        elif upDown < 0:
            print("DOWN")
            
            if move_to > -1:
              move_to -= 0.05
            UB.SetServoPosition4(move_to)

        #servo left right
        leftRight = -joystick.get_axis(False)
        if leftRight > 0:
            print("Left")
           
            if move_to < 0.9:
                move_to += 0.01
            UB.SetServoPosition3(move_to)
                
        elif leftRight < 0:
            print("Right")
            
            if move_to > -1:
              move_to -= 0.01
            UB.SetServoPosition3(move_to)

for i in range(1000):
    UB.SetServoPosition3(0)
    time.sleep(0.5)
    UB.SetServoPosition3(9000)
    time.sleep(0.5)
    UB.SetServoPosition3(-3000)
    UB.SetServoPosition4(0)
    time.sleep(0.5)
    UB.SetServoPosition4(3000)
    time.sleep(0.5)
    UB.SetServoPosition4(-3000)
