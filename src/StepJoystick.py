"""
Created on Sun Sep 13 15:46:21 2020

@author: Giglio
"""
import serial
import time
from pynput.keyboard import Key, Controller
from directkeys import PressKey, ReleaseKey, W

keyboard = Controller()

arduino = serial.Serial('COM3', 9600)

def change_old_value(value):
    if value == 1:
        return 0
    else: 
        return 1

time.sleep (1.5)

print("--------------START-------------\n")

#init step sensor state  
actual_state = int( arduino.readline() )
changed_state = change_old_value(actual_state)

while True:
    
    #get actual step state
    actual_state = int( arduino.readline() )
        
    print("-->", changed_state, " =?= ", actual_state, 
          "\nread: ", int( arduino.readline() ))
    
    #walk everytime step sensor change his state
    if actual_state != changed_state:
        PressKey(W)
        changed_state = change_old_value(changed_state)
    else:
        ReleaseKey(W)

    