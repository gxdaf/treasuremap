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
import json
from dicexpec import c
import shutil
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

a = datetime.datetime.now()

if os.path.exists("C:\TreasureMap"):
    pass
else:
    os.mkdir("C:\TreasureMap")
    os.mkdir("C:\TreasureMap\Downloads")


tx_selic = 0

option = Options()
option.set_preference("browser.download.folderList", 2)
option.set_preference("browser.download.useDownloadDir", True)
option.set_preference("browser.download.dir", "C:\TreasureMap\Downloads\IPCA")
option.set_preference("browser.download.viewableInternally.enabledTypes", "")
option.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/vnd.ms-excel, text/csv;charset=UTF-8")
#option.headless = True
driver = webdriver.Firefox(options=option)

def expec_merc(e):
    
    t = c.get(e)
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
    data_mod = a
    '''
    dif = data_mod - a 
    if dif.total_seconds > 2600000:
        espec = df_full.to_dict()
        print(df_full)
    else:
        print('Atualizado recentemente.')
    '''

def selic():
    url_sa = c.get('url')['selic_meta']
    driver.get(url_sa)
    time.sleep(2)
    xpath_sa = driver.find_element_by_xpath('//*[@id="historicotaxasjuros"]')
    xpath_sa = xpath_sa.get_attribute('outerHTML')
    soup = BeautifulSoup(xpath_sa, 'html.parser')
    tx_selic = soup.find_all('td')[4].get_text()
    return tx_selic

def download(path, ext, xpath): 
     with os.scandir(path) as it:
        for entry in it:
            if ext in entry.name and entry.is_file():
                b = datetime.datetime.fromtimestamp(os.path.getmtime(f'C:\TreasureMap\Downloads\{entry}'))
                c = a - b
                if c.total_seconds < 2600000:
                    pass
            click = xpath
            return click

def changeDir(file, dest):
    if os.path.exists(dest) is False:
        os.mkdir(dest)
    shutil.move(file, dest)

def ipca():
    url_ipca = c.get('url')['ipca_atual']
    driver.get(url_ipca)
    time.sleep(3)
    driver.find_element_by_xpath(c.get('cliques')['ipca']).click()
    time.sleep(5)
    slt =  Select(driver.find_element_by_xpath('//*[@id="tabelasidra20185213352858export"]')).select_by_value('.csv')
    download('C:\TreasureMap\Downloads', '.csv', slt)


#expec_merc('pib')
#onjs = json.dumps(espec)
#fp = open('taxas.json', 'w')
#fp.write(onjs)
#fp.close()