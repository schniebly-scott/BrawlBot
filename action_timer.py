import pyautogui
from time import sleep
import actions


def main():
    initializeBot()
    countdownToStart(10)

    #actions.jumpForwards()

def initializeBot():
    #initialized pyautogui
    pyautogui.FAILSAFE = True

def countdownToStart(time):
    #countdown
    print("Starting",end="")
    for i in range(0,time):
        print(".{}.".format(i),end="")
        sleep(1)
    print("Go")

if __name__ == "__main__":
    main()

