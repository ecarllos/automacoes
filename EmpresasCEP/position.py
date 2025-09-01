import pyautogui
import time
import keyboard
import sys

def pr():
    
    print("X")

def pd():
    print("0")



while True:
    # time.sleep(1.5)
    # print(pyautogui.position())
    pd()
    pr()


    if keyboard.is_pressed("esc"):
        sys.exit()
    
# pyautogui.dragTo(900, 300, button='left')
