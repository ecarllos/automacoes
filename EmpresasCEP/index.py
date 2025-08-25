import pyautogui
import time


time.sleep(5)
# print(pyautogui.position())

# pyautogui.click(x=317, y=656) # Posição da 1° empresa
pyautogui.press("down")
pyautogui.hotkey("ctrl" + "c")

time.sleep(5)

pyautogui.hotkey("ctrl" + "v")
