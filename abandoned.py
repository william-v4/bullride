import RPi.GPIO as gpio
from os import system
from multiprocessing import process
from time import sleep
gpio.setMode(gpio.BCM)
rotor = 16
servopin = 12
gpio.setup(rotor, gpio.OUT)
gpio.setup(servopin, gpio.OUT)
servo = gpio.pwm(servopin, gpio.OUT)
servo.start(0)
gpio.output(rotor, gpio.LOW)


def music(init):
    global play
    play = 0
    if init == 1:
        system("mpv start.wav")
    else:
        system("mpv loop.wav")
    play = 1


def rotorspin(init):
    if init ==1:
        sleep(3)
