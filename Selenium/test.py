from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium2df_locate_element import selenium2dfwait, locate_element
import time

# Configuração do Chrome
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

navegador = webdriver.Chrome(service=Service(), options=chrome_options)
selenium2dfwait.driver = navegador

wait = WebDriverWait(navegador, 40)

try:
    # Abre o site
    navegador.get("https://app.simplificagestao.com.br/ords/r/api/simplifica/login_desktop")

    # Login
    navegador.find_element(By.ID, "P101_USERNAME").send_keys("CARLOS.ALMEIDA")
    navegador.find_element(By.ID, "P101_PASSWORD").send_keys("Deborah")
    navegador.find_element(By.ID, "P101_LOGIN").click()

    # Aba de Pesquisa
    abaPesquisa = wait.until(EC.element_to_be_clickable((By.ID, "t_TreeNav_3")))
    abaPesquisa.click()

    # Razão Social
    razaoSocial = navegador.find_element(By.ID, "P146_NOME")
    razaoSocial.send_keys(Keys.CONTROL, "v")

    # Botão de Pesquisa
    botaoPesquisa = navegador.find_element(By.ID, "B2499226662932143290")
    botaoPesquisa.click()

    # Clica na primeira lupinha
    lupinhas = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'td[headers="lista_pessoa_LINK"] a')))
    lupinhas[0].click()

    # Extrai elementos HTML em DataFrame
    df_all = locate_element()
    df_all, df_links = locate_element(
        checkdf=lambda df: df.loc[df.aa_localName == 'a'],
        query='*',
        timeout=30,
        withmethods=True
    )

    print(df_all.head())
    print(df_links.head())

finally:
    navegador.quit()
