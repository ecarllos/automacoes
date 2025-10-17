import undetected_chromedriver as uc
from selenium2df_locate_element import selenium2dfwait, locate_element

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# Inicia o Chrome com detecção furtiva
navegador = uc.Chrome()
selenium2dfwait.driver = navegador



wait = WebDriverWait(navegador, 40) # Pausa dinâmica que espera 10 seg. até que uma ação seja executada, caso contrário dará ERRO.





# Abre o site
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
















# Retorna todos os elementos da página em formato DataFrame
df_all = locate_element()

# Filtra apenas elementos <a> (links)
df_all, df_links = locate_element(
    checkdf=lambda df: df.loc[df.aa_localName == 'a'],
    query='*',
    timeout=30,
    withmethods=True
)

print(df_all.head())     # Mostra todos os elementos
print(df_links.head())   # Mostra apenas os links