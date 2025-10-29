from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium2df_locate_element import selenium2dfwait, locate_element
import pandas as pd
import time

# -------------------------------------------------------------------------
# CONFIGURAÇÃO DE EXIBIÇÃO DO PANDAS (MOSTRAR TUDO)
# -------------------------------------------------------------------------
pd.set_option("display.max_rows", 100)         # mostra até 100 linhas
pd.set_option("display.max_columns", None)     # mostra todas as colunas
pd.set_option("display.width", 1000)           # define largura para evitar quebra feia
pd.set_option("display.max_colwidth", None)    # mostra o conteúdo completo das células

# -------------------------------------------------------------------------
# CONFIGURAÇÃO DO CHROME
# -------------------------------------------------------------------------
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--log-level=3")  # 0=ALL, 3=ERROR
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

navegador = webdriver.Chrome(service=Service(), options=chrome_options)
selenium2dfwait.driver = navegador
wait = WebDriverWait(navegador, 40)

try:
    # ---------------------------------------------------------------------
    # ABRE O SITE E FAZ LOGIN
    # ---------------------------------------------------------------------
    navegador.get("https://app.simplificagestao.com.br/ords/r/api/simplifica/login_desktop")

    navegador.find_element(By.ID, "P101_USERNAME").send_keys("CARLOS.ALMEIDA")
    navegador.find_element(By.ID, "P101_PASSWORD").send_keys("Deborah")
    navegador.find_element(By.ID, "P101_LOGIN").click()

    # ---------------------------------------------------------------------
    # ABRE A ABA DE PESQUISA
    # ---------------------------------------------------------------------
    abaPesquisa = wait.until(EC.element_to_be_clickable((By.ID, "t_TreeNav_3")))
    abaPesquisa.click()

    # DIGITA RAZÃO SOCIAL
    razaoSocial = navegador.find_element(By.ID, "P146_NOME")
    razaoSocial.send_keys(Keys.CONTROL, "v")

    # CLICA EM PESQUISAR
    botaoPesquisa = navegador.find_element(By.ID, "B2499226662932143290")
    botaoPesquisa.click()

    # CLICA NA PRIMEIRA LUPINHA
    lupinhas = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'td[headers="lista_pessoa_LINK"] a')))
    lupinhas[0].click()

    # ---------------------------------------------------------------------
    # LOCALIZA TODOS OS ELEMENTOS DA PÁGINA COM DETALHES COMPLETOS
    # ---------------------------------------------------------------------
    print("\nColetando informações detalhadas da página... aguarde...\n")
    df_all = locate_element(query='*', timeout=30, withmethods=True)

    # Mostra uma prévia dos elementos capturados
    print("\n===== PRÉVIA DOS ELEMENTOS CAPTURADOS =====\n")
    print(df_all.head(20))  # mostra os 20 primeiros registros

    # Salva tudo em arquivo Excel (opcional)
    df_all.to_excel("elementos_completos.xlsx", index=False)
    print("\n✅ Arquivo 'elementos_completos.xlsx' salvo com sucesso!\n")

finally:
    navegador.quit()
