# Esse código tem a função de Alterar a Razão Social e os Cnpjs digitados de forma incorreta na planilha de relacionamento

import pyautogui
import time
import keyboard
import sys


# FUNÇÕES

def CodPlanilha():
    pyautogui.PAUSE = 0.3

    pyautogui.press("down") # Abaixar para ir para célula do código da empresa
    pyautogui.press("right")
    pyautogui.press("right")
    pyautogui.press("right")
    pyautogui.press("right")
    # pyautogui.press("right") # pegar o código odonto
    pyautogui.hotkey("ctrl" , "c") # Copiar o código
    pyautogui.hotkey("left")
    pyautogui.press("left")
    pyautogui.press("left")
    pyautogui.press("left")
    # pyautogui.press("left") # pegar o código odonto
    pyautogui.hotkey("alt" , "tab") # Mudar para página do Hapvida
    time.sleep(1)


def pegarSenha():
    print("a")

def LogarHap():
    pyautogui.PAUSE = 0.3
    pyautogui.press(["tab","tab","tab","tab","tab","tab","tab"], interval=0.3) # Selecionar o label do código
    pyautogui.hotkey("ctrl" , "v") # Cola o código copiado na tela anterior
    pyautogui.press("tab") # Vai pro campo de senha
    time.sleep(0.5)
    pyautogui.press("tab")
    # pyautogui.write("575887") # Senha do SEC
    pegarSenha()
    pyautogui.press(["tab","tab"]) # Vai pro campo de Enviar
    pyautogui.press("enter")
    time.sleep(1.5) # Pause para eu clicar no botão de enviar  
    pyautogui.click(x=1577, y=244) # Clicar na tela parar poder scrollar
    pyautogui.scroll(-500000) # Scrollar totalmente pra baixo
    pyautogui.scroll(-500000) 
    pyautogui.scroll(-500000) 
    pyautogui.scroll(-500000) 
    pyautogui.scroll(-500000) 
    pyautogui.scroll(-500000) 
    pyautogui.scroll(-500000) 
    pyautogui.scroll(-500000) 
    pyautogui.scroll(200) # Scrollar pra cima até o botão ficar visível
    pyautogui.click(x=629, y=160) # Clicar em avançar
    pyautogui.click(x=850, y=484) # Etapa de confirmação extra
    time.sleep(1) # esperar pra página carregar
    pyautogui.scroll(1000) # Scrolla pra até a parte de cima da página


def PegarCnpj():
    pyautogui.PAUSE = 0.3
    pyautogui.click(x=1311, y=264) # Abrir a parte de informações da empresa
    pyautogui.doubleClick(x=932, y=306) # Selecionar o CNPJ
    pyautogui.hotkey("ctrl" , "c") # Copiar o CNPJ
    pyautogui.click(x=1290, y=217) # Sair da seção 
    time.sleep(1)
    pyautogui.hotkey("alt" , "tab") # Mudar para planilha
    pyautogui.hotkey("ctrl" , "v") # Colar o CNPJ


time.sleep(7)

while True:
    # PEGAR O CÓDIGO NA PLANILHA
    CodPlanilha()

    # LOGAR NO HAPVIDA
    LogarHap()

    # PEGAR O CNPJ
    PegarCnpj()

    if keyboard.is_pressed('esc'): # Determina o "fim" da função
        sys.exit()

