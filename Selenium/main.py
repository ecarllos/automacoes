from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# importar o navegador
navegador = webdriver.Chrome()

wait = WebDriverWait(navegador, 10) # Pausa dinâmica que espera 10 seg. até que uma ação seja executada, caso contrário dará ERRO.

# acessar um site
navegador.get("https://app.simplificagestao.com.br/ords/r/api/simplifica/login_desktop")

# colocar o navegador em tela cheia
navegador.maximize_window()

# escrever em algum campo ou formulário
navegador.find_element(By.ID, "P101_USERNAME").send_keys("CARLOS.ALMEIDA") # login
navegador.find_element(By.ID, "P101_PASSWORD").send_keys("Deborah") # senha

botao_logar = navegador.find_element(By.ID, "P101_LOGIN")

# Clicar 
botao_logar.click()



# Aba de Pesquisa
abaPesquisa = navegador.find_element(By.ID, "t_TreeNav_3")
abaPesquisa.click()

# Razão Social no Sistema
razaoSocial = navegador.find_element(By.ID, "P146_NOME")
razaoSocial.send_keys(Keys.CONTROL, "v")

# Botão de Pesquisa
botaoPesquisa = navegador.find_element(By.ID, "B2499226662932143290")
botaoPesquisa.click()

# Seleciona a Primeira "lupinha" para Abrir a Empresa
lupinhas = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'td[headers="lista_pessoa_LINK"] a')))
lupinhas[0].click()

# Selecionar o Campo de AÇÕES
acoes = wait.until(EC.presence_of_element_located((By.ID, "B2441611845714781178")))
acoes.click()

# Selecionar o botão de consultor
trocaConsultor = wait.until(EC.presence_of_element_located((By.ID, "B4175794322982668587")))
trocaConsultor.click()

# Selecionar o label de consultores
labelConsultor = wait.until(EC.presence_of_all_elements_located((By.ID, "P578_CONSULTOR_NOVO_lov_btn")))
labelConsultor.click()

# Selecionar o novo Consultor
jorge = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li[data-id='JORGE.FILHO']")))
jorge.click()

# helaine = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li[data-id='HELAINE.BRITO']")))
# helaine.click()
# augusto = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li[data-id='AUGUSTO.MATIAS']")))
# augusto.click()

# Confirmar a troca de consultor
confirmarTroca = wait.until(EC.presence_of_all_elements_located((By.ID, "B2496065396947439746")))
confirmarTroca.click()

time.sleep(10)