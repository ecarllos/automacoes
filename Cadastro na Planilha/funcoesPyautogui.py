import pyautogui
import time

time.sleep(3) # Espera 2 segundos para fazer alguma ação
pyautogui.PAUSE = 1 # Define que a cada ação terá um intervalo de 3 segundos de uma para outra
# print(pyautogui.position()) # Pegar a posição do mouse
# print(pyautogui.size()) # Pegar o tamanho da tela        1920x1080

# #Funções do Mouse
# pyautogui.click(x=500, y=500) # Clicar com o mouse
# pyautogui.moveTo(x=345, y=902, duration = 1) # Mover o mouse

# #Funções do Teclado
# pyautogui.write("Eu amo minha namorada") # escreve na tela 
# pyautogui.hotkey("Alt", "Tab") # Clica em mais de uma tecla
# pyautogui.press("win") # Pressionar alguma tecla
