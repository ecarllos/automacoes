# Esse código tem a função de Alterar a Razão Social e os Cnpjs digitados de forma incorreta na planilha de relacionamento
import pyautogui
import time
import keyboard
import sys

pyautogui.PAUSE = 1.5
time.sleep(7)

while True:
    # PEGAR O CÓDIGO NA PLANILHA
    pyautogui.press("down") # Abaixar para ir para célula do código da empresa
    pyautogui.press("right")
    pyautogui.press("right")
    pyautogui.press("right")
    pyautogui.press("right")
    pyautogui.hotkey("ctrl" , "c") # Copiar o código
    pyautogui.hotkey("left")
    pyautogui.press("left")
    pyautogui.press("left")
    pyautogui.press("left")
    # pyautogui.hotkey("alt" , "tab") # Mudar para página do Hapvida

    # time.sleep(2)

    # # LOGAR NO HAPVIDA

    # pyautogui.press(["tab","tab","tab","tab","tab","tab","tab"], interval=0.5) # Selecionar o label do código
    # pyautogui.hotkey("ctrl" , "v") # Cola o código copiado na tela anterior
    # pyautogui.press("tab") # Vai pro campo de senha
    # pyautogui.press("tab")
    # pyautogui.write("197547") # Senha do SEC
    # pyautogui.press(["tab","tab"]) # Vai pro campo de Enviar
    # pyautogui.press("enter")

    # time.sleep(6) # Pause para eu clicar no botão de enviar

    # # PEGAR O CNPJ
    # pyautogui.click(x=1311, y=264) # Abrir a parte de informações da empresa
    # pyautogui.doubleClick(x=932, y=306) # Selecionar o CNPJ
    # pyautogui.hotkey("ctrl" , "c") # Copiar o CNPJ
    # pyautogui.click(x=1290, y=217) # Sair da seção 
    # pyautogui.hotkey("alt" , "tab") # Mudar para planilha

    # # COLAR CNPJ NA PLANILHA
    # pyautogui.hotkey("ctrl" , "v") # Colar o CNPJ

    if keyboard.is_pressed('esc'): # Determina o "fim" da função
        sys.exit()