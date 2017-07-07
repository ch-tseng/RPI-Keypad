#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

btnPin = [2, 3, 4] #G, Y, R

file = open('/boot/exam.txt')
questions = file.readlines()
file.close()

print (len(questions))
print questions[2]
#for line in file:
#     print line

file.close()
