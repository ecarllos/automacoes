import pyautogui
import time

pyautogui.PAUSE = 2
time.sleep(4)
print(pyautogui.position())


# pyautogui.click(x=317, y=656) # Posição da 1° empresa
# pyautogui.press("down")
pyautogui.hotkey("ctrl" , "c")

time.sleep(3)
print(pyautogui.position())
pyautogui.hotkey("ctrl" , "v")
