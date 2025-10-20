from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium2df_locate_element import selenium2dfwait, locate_element
import pandas as pd
import math
import time
from rich.console import Console
from rich.table import Table

# ========================= CONFIGURAÇÕES INICIAIS ========================= #

# Configuração do pandas (para exibir todos os dados sem truncar ao salvar)
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 0)
pd.set_option("display.max_colwidth", None)

console = Console()

# Função para exibir o DataFrame de forma paginada e legível
def exibir_dataframe(df, linhas_por_tela=25, colunas_por_tela=8):
    total_linhas = len(df)
    total_telas = math.ceil(total_linhas / linhas_por_tela)

    console.print(f"[bold cyan]Total de linhas:[/bold cyan] {total_linhas}")
    console.print(f"[bold cyan]Total de colunas:[/bold cyan] {len(df.columns)}")
    console.print(f"[bold yellow]Exibindo {linhas_por_tela} por tela[/bold yellow]\n")

    for i in range(total_telas):
        inicio = i * linhas_por_tela
        fim = inicio + linhas_por_tela
        subset = df.iloc[inicio:fim]

        table = Table(show_header=True, header_style="bold magenta", title=f"Lote {i+1}/{total_telas}")

        # Adiciona as colunas limitadas
        for col in subset.columns[:colunas_por_tela]:
            table.add_column(col)

        # Adiciona as linhas
        for _, row in subset.iterrows():
            table.add_row(*[str(row[col])[:100] for col in subset.columns[:colunas_por_tela]])

        console.print(table)

        if i < total_telas - 1:
            continuar = input(f"\nPressione [Enter] para continuar ({i+1}/{total_telas}) ou 'q' para sair: ")
            if continuar.lower() == 'q':
                break

# ========================= CONFIGURAÇÃO DO NAVEGADOR ========================= #

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--log-level=3")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

navegador = webdriver.Chrome(service=Service(), options=chrome_options)
selenium2dfwait.driver = navegador
wait = WebDriverWait(navegador, 40)

# ========================= EXECUÇÃO PRINCIPAL ========================= #

try:
    console.print("[bold green]Acessando o sistema...[/bold green]")
    navegador.get("https://app.simplificagestao.com.br/ords/r/api/simplifica/login_desktop")

    console.print("[bold green]Fazendo login...[/bold green]")
    navegador.find_element(By.ID, "P101_USERNAME").send_keys("CARLOS.ALMEIDA")
    navegador.find_element(By.ID, "P101_PASSWORD").send_keys("Deborah")
    navegador.find_element(By.ID, "P101_LOGIN").click()

    console.print("[bold green]Abrindo aba de pesquisa...[/bold green]")
    abaPesquisa = wait.until(EC.element_to_be_clickable((By.ID, "t_TreeNav_3")))
    abaPesquisa.click()

    razaoSocial = navegador.find_element(By.ID, "P146_NOME")
    razaoSocial.send_keys(Keys.CONTROL, "v")

    botaoPesquisa = navegador.find_element(By.ID, "B2499226662932143290")
    botaoPesquisa.click()

    lupinhas = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'td[headers="lista_pessoa_LINK"] a')))
    lupinhas[0].click()

    console.print("[bold cyan]Extraindo elementos HTML da página...[/bold cyan]")
    df_all = locate_element()

    # Filtra elementos <a>
    df_all, df_links = locate_element(
        checkdf=lambda df: df.loc[df.aa_localName == 'a'],
        query='*',
        timeout=30,
        withmethods=True
    )

    console.print("[bold green]✔ Captura concluída![/bold green]")

    # Salva os dados completos em CSV
    df_all.to_csv("todos_elementos.csv", index=False, encoding="utf-8-sig")
    console.print("[bold yellow]Arquivo salvo como:[/bold yellow] todos_elementos.csv\n")

    # Exibe de forma legível e paginada
    exibir_dataframe(df_all, linhas_por_tela=20, colunas_por_tela=10)

except Exception as e:
    console.print(f"[bold red]Erro durante a execução:[/bold red] {e}")

finally:
    navegador.quit()
    console.print("[bold cyan]Navegador fechado com segurança.[/bold cyan]")
