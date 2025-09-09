from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# importar o navegador
navegador = webdriver.Chrome()

# acessar um site
navegador.get("https://app.simplificagestao.com.br/ords/r/api/simplifica/login_desktop")

# colocar o navegador em tela cheia
navegador.maximize_window()

# escrever em algum campo ou formulário
navegador.find_element(By.ID, "P101_USERNAME").send_keys("CARLOS.ALMEIDA") # login
navegador.find_element(By.ID, "P101_PASSWORD_CONTAINER").send_keys("Deborah") # senha

botao_logar = navegador.find_element(By.ID, "P101_LOGIN")

# Clicar 
botao_logar.click()
time.sleep(10)