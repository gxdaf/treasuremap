import os
import time
import datetime
import requests
import datetime
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox import firefox_profile, options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select
from dicexpec import c
import shutil
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

dthr = datetime.datetime.now() #Momento atual

option = Options()
option.set_preference("browser.download.folderList", 2)
option.set_preference("browser.download.useDownloadDir", True)
option.set_preference("browser.download.dir", "C:\TreasureMap\Downloads\IPCA") 
option.set_preference("browser.download.viewableInternally.enabledTypes", "")
option.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/vnd.ms-excel, text/csv;charset=UTF-8")
#option.headless = True
driver = webdriver.Firefox(options=option)

def expec_merc(e): 
    '''
    Retorna a tabela HTML das expectativas de mercado de curto prazo para a Selic Meta, o IGP-M, o PIB Total e o IPCA
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
    df_full = pd.read_html(str(tab))[0]

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

selic()

def taxas_atuais(taxa):
    '''
    Retorna os índices econômicos do ano (TR, IPCA e IGP-M)
    '''
    url_ipca = c.get('url')[taxa]
    driver.get(url_ipca)
    xpath = driver.find_element_by_xpath(c.get('atual')[0])
    cont = xpath.get_attribute('outerHTML')
    soup = BeautifulSoup(cont, 'html.parser')
    tab = soup.find(name='table')
    df_full = pd.read_html(str(tab))[0]