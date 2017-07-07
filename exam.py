#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

btnPin = [2, 3, 4] #G, Y, R

GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def btnGreen_Clicked(channel):  
    print ("Green button clicked.")  

def btnYellow_Clicked(channel):
    print ("Yellow button clicked.")

def btnRed_Clicked(channel):
    print ("Red button clicked.")

GPIO.add_event_detect(2, GPIO.FALLING, callback=btnGreen_Clicked, bouncetime=300)  
GPIO.add_event_detect(3, GPIO.FALLING, callback=btnYellow_Clicked, bouncetime=300)
GPIO.add_event_detect(4, GPIO.FALLING, callback=btnRed_Clicked, bouncetime=300)

file = open('/boot/exam.txt')
questions = file.readlines()
file.close()

print (len(questions))
print questions[2]
#for line in file:
#     print line

file.close()

raw_input("Press Enter when ready\n>") 
