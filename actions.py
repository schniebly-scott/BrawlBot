from time import sleep
from random import random
from pyautogui import keyDown, keyUp


actionList = [ #all of the possible actions

]

def jump_forwards(time=0.5):
    keyDown('w')
    keyDown('d')
    sleep(humanize(time))
    keyUp('w')
    keyUp('d')


def holdKey(key, seconds=1.00):
    keyDown(key)
    sleep(seconds)
    keyUp(key)

def humanize(num):
    div = (random() / 10) + 1
    num = num / div
    return num