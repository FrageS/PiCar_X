#!/usr/bin/python3
import numpy as np
import cv2
import sys
sys.path.append(r'/opt/ezblock')
from ezblock import __reset_mcu__
import time
import keyboard
__reset_mcu__()
time.sleep(0.01)

from picarx import dir_servo_angle_calibration
from picarx import forward
from ezblock import delay
from picarx import backward
from picarx import set_dir_servo_angle
from picarx import stop
import sys, termios, tty, os

# https://github.com/recantha/EduKit3-RC-Keyboard/blob/master/rc_keyboard.py
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

dir_servo_angle_calibration(0)
def main():
    while True:
        cap = cv2.VideoCapture(0)        
        speed = 0
        old_speed = 0
        steer = 0
        old_steer = 0
        while True: 
            ret, frame = cap.read()
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            char = getch()   
            old_speed = speed
            old_steer = steer

            # Longitudinal Control
            if (char == "w"):
                speed += 0.01
            elif (char == "s"):
                speed -= 0.01
            elif (char == "e"):
                speed = 0
            elif (char == "q"):
                exit() 
            else:
                old_speed = speed    

            if (old_speed != speed):
                print('Current speed: ', speed, 'rpm')

            forward(speed) 

            # Lateral control
            if (char == "a") and speed != 0:
                steer -= 2
            if (char == "d") and speed != 0:
                steer += 2

            if (steer > 35):
                steer = 35
            elif (steer < -35):
                steer = -35


            if (old_steer != steer):
                print("Current steer angle: ", steer, "°")
            set_dir_servo_angle((steer))

        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    try:
        main()
    except:      
        print('Program cancelled')