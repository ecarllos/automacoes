import pyautogui
import time
import keyboard
import sys

while True:
    time.sleep(1.5)
    print(pyautogui.position())

    if keyboard.is_pressed("esc"):
        sys.exit()
    
# pyautogui.dragTo(900, 300, button='left')
