from os import system
from time import sleep
from multiprocessing import Process
import sys
import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
gpio.setup(16, gpio.IN)
gpio.setup(17, gpio.IN)
stop = 0
play = 0
started = 0


def start():
    global started
    if started != 1:
        system("mpv start.wav")
        global play
        play = 1
        started = 1


def loop():
    global play
    if gpio.input(16) != 1:
        global stop
        stop = 1
    if play == 1 and started == 1:
        play = 0
        system("mpv loop.wav")
        play = 1


while True:
    if stop != 1 and gpio.input(16) == 1:
        Process(target=start()).start()
        Process(target=loop()).start()
    else:
        system("pkill mpv")
        if gpio.input(17) == 1:
            stop = 0
            play = 0
            started = 0


