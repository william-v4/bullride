import RPi.GPIO as gpio
from time import sleep
import random
import sys
import os
from multiprocessing import Process
import subprocess

gpio.setMode(gpio.board)
gpio.setup(11, gpio.OUT)
servo = gpio.pwm(11, 50)
servo.start(0)
gpio.setup(13, gpio.OUT)
enable = gpio.pwm(13, 50)
enable.start(0)
gpio.output(13, gpio.LOW)
stop = 0
gpio.setup(16, gpio.IN)


def start():
    global playfinished
    global started
    if started != 1:
        playfinished = 0
        os.system("mpv start.wav")
        playfinished = 1
    started = 1


def rotorspin():
    gpio.out(13, gpio.HIGH)


def servospin():
    servo.ChangeDutyCycle(6.25)
    servo.ChangeDutyCycle(7.5)
    servo.ChangeDutyCycle(8.75)
    servo.ChangeDutyCycle(7.5)


def stop():
    global stop
    if gpio.input(16) == 1:
        stop = 1


def ambient():
    global playfinished
    if start == 1 and playfinished == 1:
        playfinished = 0
        os.system("mpv loop.wav")
        playfinished = 1


while True:
    if gpio.input(16) == 1:
        stop = 1
        sleep(2)
    if stop != 1:
        Process(target=start()).start()
        Process(target=ambient()).start()
        sleep(3)
        Process(target=servospin()).start()
        Process.start(target=rotorspin()).start()
    else:
        if gpio.input(16) == 1:
            stop = 0
            sleep(2)
