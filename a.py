import time
import datetime
from numpy import e
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox import firefox_profile, options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select
from dicexpec import c
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from dbsql import cr_tab, drop_tab, ins_tab

dthr = datetime.datetime.now() #Momento atual

option = Options()
option.set_preference("browser.download.folderList", 2)
option.set_preference("browser.download.useDownloadDir", True)
option.set_preference("browser.download.dir", "C:\TreasureMap\Downloads\IPCA") 
option.set_preference("browser.download.viewableInternally.enabledTypes", "")
option.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/vnd.ms-excel, text/csv;charset=UTF-8")
option.headless = True
driver = webdriver.Firefox(options=option)

def acao():
    print('Qual tabela deseja consultar?')
    print('1. Expectativas do mercado;\n2. Selic Meta;\n3. IPCA;\n4. TR;\n5. IGP-M.')
    escolha = input('Insira a opção: ')
    if '1' in escolha:
        print('Qual indicador deseja consultar?\n 1. PIB;\n 2. Selic Meta;\n 3.IPCA;\n4. IGP-M.')
        escolha = input('Insira a opção: ')
        if '1' in escolha:
            expec_merc('pib')
        elif '2' in escolha:
            expec_merc('selic')
        elif '3' in escolha:
            expec_merc('ipca')
        elif '4' in escolha:
            expec_merc('igpm')
        else:
            print('Opção inexistente.')
            acao()
    elif '2' in escolha:
        selic()
    elif '3' in escolha:
        taxas_atuais('ipca')
    elif '4' in escolha:
        taxas_atuais('tr')
    elif '5' in escolha:
        taxas_atuais('igpm')
    else:
        print('Opção inexistente.')
        acao()

def to_tuple(valores=None):
    celulas = [tuple(x) for x in valores.to_records(index=False)]
    for celula in celulas:
        if '\b' in celula:
            data = celula.index('%s/%s/%s')
            print(celula[data])
    print('1. Criar tabela; \n2. Atualizar tabela;\n3. Inserir dados na tabela;\n4. Excluir tabela.\n 5. Nada')
    esc = input('Ação desejada: ')
    nome_tab = input('Insira o nome da tabela: ')
    if '1' in esc:
        tipo_col = []
        colunas = []
        troca = input(f"Deseja alterar o nome das colunas? (S/N) {valores.head()}\nNa presença de '%', '/' ou '.' no nome das colunas, recomenda-se a mudança.").upper()
        if 'S' in troca:
            troca = tuple(sorted(valores))
            for coluna in troca:
                colunas.append(input(f'Digite o nome que substituirá{coluna}').capitalize())
        else:
            colunas = tuple(sorted(valores))
        for coluna in colunas:
            tipo_col.append(input(f'Especifique o tipo da coluna {coluna}: ').upper())
            print(tipo_col)        
        cr_tab(nome_tab, colunas, tipo_col)
    elif '2' in esc:
        pass
        #att_tab('selic')
    elif '3' in esc:
        pass
        ins_tab(nome_tab, celulas)
    elif '4' in esc:
        drop_tab(nome_tab)
    elif '5' in esc:
        pass
    else: 
        print('Opção inválida.')
        to_tuple()

def expec_merc(e): 
    '''
    Retorna a tabela HTML das expectativas de mercado de curto prazo para a Selic Meta = 'selic', o IGP-M = 'igpm', o PIB Total = 'pib' e o IPCA 'ipca'
    '''
    t = c.get('expectativa')[e]
    url_se = c.get('url')['expectativa']
    driver.get(url_se)
    time.sleep(5)
    for k in range(3):
            x = driver.find_element_by_xpath(t[k][0])
            x.click()
            time.sleep(1)
            x.send_keys(t[k][1])
            time.sleep(1)
            x.find_element_by_xpath(t[k][2]).click()
            time.sleep(2)    

    driver.find_element_by_xpath(c.get('cliques')['expectativa'][0]).click()
    time.sleep(3)
    tabela = driver.find_element_by_xpath(c.get('cliques')['expectativa'][1])
    cont = tabela.get_attribute('outerHTML')
    soup = BeautifulSoup(cont, 'html.parser')
    tab = soup.find(name='table')
    th = soup.find(name= 'thead').get_text()
    df = pd.read_html(str(tab))[0]
    to_tuple(df)

def selic():
    '''
    Retorna a Selic Meta atual
    '''
    datas = []
    taxas = []
    url_sa = c.get('url')['selic_meta']
    driver.get(url_sa)
    time.sleep(2)
    xpath_sa = driver.find_element_by_xpath('//*[@id="historicotaxasjuros"]')
    xpath_sa = xpath_sa.get_attribute('outerHTML')
    soup = BeautifulSoup(xpath_sa, 'html.parser')
    data = soup.find('tbody').find_all('tr')
    for row in data:
        datas.append(row.find_all('td')[1].get_text())
        taxas.append(row.find_all('td')[4].get_text())
    hist_selic = {'Data': datas, 'Taxas': taxas}
    df = pd.DataFrame(hist_selic)
    to_tuple(df)

def taxas_atuais(taxa):
    '''
    Retorna os índices econômicos do ano (TR = 'tr', IPCA = 'ipca' e IGP-M = 'igpm')
    '''
    url_ipca = c.get('url')[taxa]
    driver.get(url_ipca)
    time.sleep(2)
    xpath = driver.find_element_by_xpath(c.get('atual')[0])
    cont = xpath.get_attribute('outerHTML')
    soup = BeautifulSoup(cont, 'html.parser')
    tab = soup.find(name='table')
    df = pd.read_html(str(tab))[0]
    cols = df.columns.values
    #da = df.rename(columns={cols[i]: cols[i][1] for i in range(len(cols))})
    for i in range(len(df.columns.values)):
        df.columns.values[i] = df.columns.values[i][1]
    to_tuple(df)

acao()