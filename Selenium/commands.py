from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# importar o navegador
navegador = webdriver.Chrome()

# acessar um site
navegador.get("https://youtube.com")

# colocar o navegador em tela cheia
navegador.maximize_window()

# pausa
# time.sleep(10)

# selecionar elementos na tela
botao_pesquisa = navegador.find_element(By.NAME, "search_query")

# Clicar 
botao_pesquisa.click()

# Escrever
botao_pesquisa.send_keys("surf medina")

# Enter
botao_pesquisa.send_keys(Keys.ENTER)

time.sleep(4)

# encontrar vários elementos
listarAbasInternas = navegador.find_elements(By.CSS_SELECTOR, ".yt-simple-endpoint.style-scope.ytd-mini-guide-entry-renderer")
inicio = navegador.find_element(By.ID, "endpoint")
# inicio.click()

for botao in listarAbasInternas:
    if botao.get_attribute("aria-label") == "Início":
        botao.click()
        break



# selecionar uma aba
# abas = navegador.window_handles # Declara todas as abas abertas

# # navegar pelas abas
# navegador.switch_to.window(abas[1])

# # navegar para um site diferente
# navegador.get("https://www.youtube.com/")

# # escrever em algum campo ou formulário
# navegador.find_element(By.ID, "P101_USERNAME").send_keys("CARLOS.ALMEIDA")
# navegador.find_element(By.ID, "P101_PASSWORD_CONTAINER").send_keys("Deborah")

time.sleep(200)