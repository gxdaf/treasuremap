import time
import datetime
from numpy import e
import numpy
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
from dbsql import cr_tab, drop_tab, ins_tab, att_tab
import dateutil.parser as dparser

dthr = datetime.datetime.now() #Momento atual

def acao():
    print('Qual tabela deseja consultar?')
    print('1. Expectativas do mercado;\n2. Selic Meta;\n3. IPCA;\n4. TR;\n5. IGP-M;\n6. TPFs;\n7. Sair.')
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
    elif '6' in escolha:
        tpf()
    elif '7' in escolha:
        run = False
    else:
        print('Opção inexistente.')
        acao()

option = Options()
option.set_preference("browser.download.folderList", 2)
option.set_preference("browser.download.useDownloadDir", True)
option.set_preference("browser.download.dir", "C:\TreasureMap\Downloads\IPCA") 
option.set_preference("browser.download.viewableInternally.enabledTypes", "")
option.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/vnd.ms-excel, text/csv;charset=UTF-8")
option.headless = True
driver = webdriver.Firefox(options=option)

def limpeza(valores=None):
    celulas = [list(x) for x in valores.to_records(index=False)]
    print('1. Criar tabela; \n2. Atualizar tabela;\n3. Inserir dados na tabela;\n4. Excluir tabela.\n 5. Nada')
    esc = input('Ação desejada: ')
    nome_tab = input('Insira o nome da tabela: ')
    if '1' in esc:
        tipo_col = []
        colunas = []
        troca = input(f"Deseja alterar o nome das colunas? (S/N) {valores.head()}\nNa presença de '%', '/', '.', números e/ou acentuação gráfica no nome das colunas, recomenda-se a mudança. ").upper()
        if 'S' in troca:
            troca = tuple(sorted(valores))
            for coluna in troca:
                colunas.append(input(f'Digite o nome que substituirá {coluna}'))
        else:
            colunas = tuple(sorted(valores))
        for coluna in colunas:
            tipo_col.append(input(f'Especifique o tipo da coluna {coluna}: ').upper())     
        cr_tab(nome_tab, colunas, tipo_col)
    elif '2' in esc:
        pass
        att_tab(tabela)
    elif '3' in esc:
        print(valores.head)
        esc = input('Limpar células? (S/N)').upper()
        if 'S' in esc:
            for celula in celulas:
                for i in range(len(celula)):
                    if isinstance(celula[i], numpy.int64) == True or isinstance(celula[i], numpy.float64) == True:
                            celula[i] = str(celula[i])
                            if 'nan' in celula[i]:
                                celula[i] = 'NULL'
                            else:
                                if '.' not in celula[i]:
                                    celula[i] = celula[i][:3]
                                    celula[i] = f'{celula[i][:1]}.{celula[i][1:]}'
                                celula[i] = float(celula[i])
                    elif isinstance(celula[i], numpy.float64) == False or isinstance(celula[i], numpy.int64) == False or isinstance(celula[i], float) == False:
                        if '/' in celula[i]:
                            dt = celula[i].split('/')
                            dt[0], dt[-1] = dt[-1], dt[0]
                            celula[i] = '-'.join(dt)
                            celula[i] = f"'{celula[i]}'"
                        elif (len(celula[i]) == 0):
                            celula[i] = 'NULL'
                        if '%' in celula[i]:
                            celula[i] = celula[i].translate({ord('%'): None})
                        if 'R$' in celula[i]:
                            celula[i] = celula[i].translate({ord('R'): None})
                            celula[i] = celula[i].translate({ord('$'): None})
                        if ',' in celula[i] and (r'^\w*' in celula[i]):
                            celula[i] = celula[i].replace(',', '.')
                            celula[i] = float(celula[i])
                        if isinstance(celula[i], str) == True and '-' not in celula[i]:
                            celula[i] = f"'{celula[i]}'"
        ins_tab(nome_tab, celulas)
    elif '4' in esc:
        drop_tab(nome_tab)
    elif '5' in esc:
        run = False
    else: 
        print('Opção inválida.')
        limpeza()

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

    driver.find_element_by_xpath(c.get('cliques')['expectativa'][e][0]).click()
    time.sleep(3)
    tabela = driver.find_element_by_xpath(c.get('cliques')['expectativa'][e][1])
    cont = tabela.get_attribute('outerHTML')
    soup = BeautifulSoup(cont, 'html.parser')
    tab = soup.find(name='table')
    th = soup.find(name= 'thead').get_text()
    df = pd.read_html(str(tab))[0]
    limpeza(df)

def tpf():
    url = 'https://www.tesourodireto.com.br/titulos/precos-e-taxas.htm'
    driver.get(url)
    time.sleep(2)
    xpath_sa = driver.find_element_by_xpath('/html/body/main/div[1]/div[2]/div/div/div/div[1]/div/div[9]/table')
    xpath_sa = xpath_sa.get_attribute('outerHTML')
    soup = BeautifulSoup(xpath_sa, 'html.parser')
    data = soup.find('table')
    df = pd.read_html(str(data))[0]
    df = df.drop(columns='Unnamed: 5')
    limpeza(df)


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
    limpeza(df)

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
    print(df)
    limpeza(df)

run = True

while run:
    acao()
