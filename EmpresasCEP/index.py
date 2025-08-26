import pyautogui
import time

pyautogui.PAUSE = 1.5
time.sleep(5)

# PEGAR O CÓDIGO NA PLANILHA
pyautogui.press("down") # Abaixar para ir para célula do código da empresa
pyautogui.hotkey("ctrl" , "c") # Copiar o código
pyautogui.hotkey("ctrl" , "tab") # Mudar para página do Hapvida

time.sleep(3)

# LOGAR NO HAPVIDA

pyautogui.press(["tab","tab","tab","tab","tab","tab","tab"], interval=0.5) # Selecionar o label do código
pyautogui.hotkey("ctrl" , "v") # Cola o código copiado na tela anterior
pyautogui.press("tab") # Vai pro campo de senha
pyautogui.press("tab")
pyautogui.write("197547") # Senha do SEC
pyautogui.press(["tab","tab"]) # Vai pro campo de Enviar
pyautogui.press("enter")

time.sleep(6) # Pause para eu clicar no botão de enviar

# PEGAR O CNPJ
pyautogui.click(x=1311, y=264) # Abrir a parte de informações da empresa
pyautogui.doubleClick(x=932, y=306) # Selecionar o CNPJ
pyautogui.hotkey("ctrl" , "c") # Copiar o CNPJ
pyautogui.click(x=1290, y=217) # Sair da seção 

pyautogui.hotkey("ctrl" , "tab") # Mudar para página do Simplifica


# PESQUISAR A EMPRESA
pyautogui.click(x=1622, y=233) # Selecionar a parte do CNPJ
pyautogui.hotkey("ctrl" , "a") # Selecionar o CNPJ antigo que foi deixado
pyautogui.hotkey("ctrl" , "v") # Colar o CNPJ
pyautogui.press("enter") # Procurar o cnpj

