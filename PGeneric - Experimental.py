import pyautogui
import time
from random import *
import winsound
import os

def intro():
    random = 0
    inn = input("How Many times should I run this code?")
    time.sleep(5)
    while (int(random) < int(inn)):
        execute()
        #print("CURRENT RANDOM VALUE = " + str(random))
        random = random + 1

def execute():
    global hours
    global minutes
    hours = randint(1, 12)
    minutes = randint(1, 59)
    #seconds = randint(1, 59)
    #pyautogui.typewrite(str(hours))
    hour()
    tab()
    #pyautogui.typewrite(str(minutes))
    minute()
    tab()
    #pyautogui.typewrite(str(seconds))
    #tab()
    AMPM()
    tab()
    tab()
    tab()
    tab()


def hour():
    if (hours == 1):
        pyautogui.typewrite('01')
    if (hours == 2):
        pyautogui.typewrite('02')
    if (hours == 3):
        pyautogui.typewrite('03')
    if (hours == 4):
        pyautogui.typewrite('04')
    if (hours == 5):
        pyautogui.typewrite('05')
    if (hours == 6):
        pyautogui.typewrite('06')
    if (hours == 7):
        pyautogui.typewrite('07')
    if (hours == 8):
        pyautogui.typewrite('08')
    if (hours == 9):
        pyautogui.typewrite('09')
    else:
        pyautogui.typewrite(str(hours))

def minute():
    if (minutes == 1):
        pyautogui.typewrite('01')
    if (minutes == 2):
        pyautogui.typewrite('02')
    if (minutes == 3):
        pyautogui.typewrite('03')
    if (minutes == 4):
        pyautogui.typewrite('04')
    if (minutes == 5):
        pyautogui.typewrite('05')
    if (minutes == 6):
        pyautogui.typewrite('06')
    if (minutes == 7):
        pyautogui.typewrite('07')
    if (minutes == 8):
        pyautogui.typewrite('08')
    if (minutes == 9):
        pyautogui.typewrite('09')
    else:
        pyautogui.typewrite(str(minutes))
        
def AMPM():
    if (hours == 1) or (hours == 2) or (hours == 3) or (hours == 4) or (hours == 5) or (hours == 6) or (hours == 12):
        pyautogui.typewrite("PM")
    else:
        pyautogui.typewrite("AM")

def tab():
    pyautogui.press('tab')

def beep():
    winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)

def end():
        beep()
        print("The script has ended")

def cls():
        os.system('cls')

def do_task():
    intro()
    cls()
    end()
    cls()
    rerun()
    
def rerun():
    while True:
        ans = input("Do you want to go again? Press Y or N.").upper()
        if ans == "Y":
                do_task()
        if ans == "N":
                print("Goodbye!")
                time.sleep(1.5)
                quit()

do_task()
