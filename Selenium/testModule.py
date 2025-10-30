import undetected_chromedriver as uc
from selenium2df_locate_element import selenium2dfwait, locate_element
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Inicia o Chrome com detecção furtiva
navegador = uc.Chrome()
selenium2dfwait.driver = navegador



wait = WebDriverWait(navegador, 10) # Pausa dinâmica que espera 10 seg. até que uma ação seja executada, caso contrário dará ERRO.


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
# razaoSocial.send_keys(Keys.CONTROL, "v") # Cola a empresa 
razaoSocial.send_keys("HENDERSON SABINO MOURA SILVA") # Digita a empresa diretamente


# Botão de Pesquisa
botaoPesquisa = navegador.find_element(By.ID, "B2499226662932143290")
botaoPesquisa.click()

# Seleciona a Primeira "lupinha" para Abrir a Empresa
lupinhas = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'td[headers="lista_pessoa_LINK"] a')))
lupinhas[0].click()

# Clica nas ações (Pega o aa_innerText "Ações")
acoes = navegador.find_element(By.XPATH, f"//*[contains(normalize-space(text()), '{"Ações"}')]") # aa_innertext
acoes.click()

# Clica em troca de consultor
trocaConcultor = navegador.find_element(By.ID, "B4175794322982668587") 
trocaConcultor.click()

# botaoConsultor = navegador.find_element(By.ID, "P578_CONSULTOR_NOVO_CONTAINER")
# botaoConsultor.click()

# Retorna todos os elementos da página em formato DataFrame
df_all = locate_element()

# Filtra apenas elementos <a> (links)
df_all, df_but = locate_element(
    checkdf=lambda db: db.loc[db.aa_localName == 'button'],
    query='*',
    timeout=30,
    withmethods=True
)

df = df_but

# 2️⃣ Lista das colunas úteis (as que realmente ajudam a entender o elemento)
colunas = [
    'role',               # função semântica (ex: button, link, checkbox)
    'aa_innerText',       # texto interno visível
    'tag',                # tipo de elemento (div, span, input, a, button, etc.)
    'id',                 # id único (se existir)
    'name',               # atributo name (muito usado em formulários)
    'class',              # classes CSS (excelente pra identificar grupos de elementos)
    'type',               # tipo de input (text, password, submit, etc.)
    'text',               # texto interno visível do elemento
    'aa_tagName',         # tipo do elemento (a, div, span, input, etc.)
    'aa_id',              # id único (quando existe)
    'aa_className',       # classes aplicadas (útil para identificar botões, textos, etc.)
    'aa_textContent',     # texto bruto (inclui quebras e espaços)
    'aa_href',            # link (se existir)
    'aa_outerHTML',       # estrutura HTML completa do elemento
    'screenshot_path',     # caminho da captura de tela
    'value',              # valor de inputs e botões
    'placeholder',        # placeholder de inputs
    'aria-label',         # acessibilidade — frequentemente usado para identificar botões
    'title'  
]

# 3️⃣ Mantém só essas colunas (as que realmente importam)
df_limpo = df[[c for c in colunas if c in df.columns]]

# 4️⃣ Remove linhas completamente vazias (às vezes aparecem)
df_limpo = df_limpo.dropna(how='all')

# 5️⃣ Salva o resultado em dois formatos
df_limpo.to_csv('elementos.csv', index=False, encoding='utf-8-sig')

# 6️⃣ Mostra no terminal um resumo do que foi salvo
print(f"Arquivo CSV e XLSX gerados com {len(df_limpo)} elementos úteis.")



# Fecha o navegador
navegador.quit()