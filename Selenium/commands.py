from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# importar o navegador
navegador = webdriver.Chrome()

# acessar um site
navegador.get("https://app.simplificagestao.com.br/ords/r/api/simplifica/login_desktop ")

# colocar o navegador em tela cheia
navegador.maximize_window()

# pausa
time.sleep(10)

# selecionar elementos na tela
botao_logar = navegador.find_element(By.ID, "P101_LOGIN")

# Clicar 
botao_logar.click()

# encontrar vários elementos
listar_botoes = navegador.find_elements(By.ID, "P101_LOGIN")

for botao in listar_botoes:
    if "Nome" in botao.text:
        botao.click()
        break



# selecionar uma aba
abas = navegador.window_handles # Declara todas as abas abertas

# navegar pelas abas
navegador.switch_to.window(abas[1])

# navegar para um site diferente
navegador.get("https://www.youtube.com/")

# escrever em algum campo ou formulário
navegador.find_element(By.ID, "P101_USERNAME").send_keys("CARLOS.ALMEIDA")
navegador.find_element(By.ID, "P101_PASSWORD_CONTAINER").send_keys("Deborah")

time.sleep(10)