import pyautogui

pyautogui.PAUSE = 3 # Define que a cada ação terá um intervalo de 3 segundos de uma para outra
print(pyautogui.position()) # Pegar a posição do mouse
print(pyautogui.size()) # Pegar o tamanho da tela
pyautogui.click(x=500, y=500) # Clicar com o mouse
pyautogui.moveTo(x=345, y=902, duration = 1) # Mover o mouse
