from os import name
import time
import requests
import datetime
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox import firefox_profile, options
from selenium.webdriver.firefox.options import Options
import json
from dicexpec import c
import os.path

option = Options()
option.set_preference("browser.download.folderList", 2)
option.set_preference("browser.download.dir", "C:\Downloads")
option.set_preference("browser.download.useDownloadDir", True)
option.set_preference("browser.download.viewableInternally.enabledTypes", "")
option.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/vnd.ms-excel")
#option.headless = True
driver = webdriver.Firefox(options=option)

'''
url_se = 'https://www3.bcb.gov.br/expectativas2/#/consultaSeriesEstatisticas'
driver.get(url_se)
''' 
time.sleep(5)

'''
def expec_merc(e):
    t = c.get(e)
    for k in range(3):
            x = driver.find_element_by_xpath(t[k][0])
            x.click()
            time.sleep(1)
            x.send_keys(t[k][1])
            time.sleep(1)
            x.find_element_by_xpath(t[k][2]).click()
            time.sleep(2)    

    driver.find_element_by_xpath('/html/body/app-root/div/app-main/main/div/app-consulta-serie-estatisticas/section/div[2]/div[3]/button').click()
    time.sleep(3)
    tabela = driver.find_element_by_xpath('/html/body/app-root/div/app-main/main/div/app-consulta-serie-estatisticas/app-detalhe-series-estatisticas/div/section/div/div[2]/div[2]/div[2]/tabset/div/tab/app-series-estatisticas-indicador/div/tabset/div/tab[1]/div/table')
    cont = tabela.get_attribute('outerHTML')
    soup = BeautifulSoup(cont, 'html.parser')
    tab = soup.find(name='table')
    th = soup.find(name= 'thead').get_text()
    df_full = pd.read_html(str(tab))[0]


espec = df_full.to_dict()
onjs = json.dumps(espec)
fp = open('taxas.json', 'w')
fp.write(onjs)
fp.close()

url_sa = 'https://www.bcb.gov.br/controleinflacao/historicotaxasjuros'
driver.get(url_sa)
time.sleep(2)
xpath_sa = driver.find_element_by_xpath('//*[@id="historicotaxasjuros"]')
xpath_sa = xpath_sa.get_attribute('outerHTML')
soup = BeautifulSoup(xpath_sa, 'html.parser')
selic = soup.find_all('td')[4].get_text()
'''

url_jurcred = 'https://www.bcb.gov.br/estatisticas/txjuros'
driver.get(url_jurcred)
time.sleep(5)
link = driver.find_element_by_xpath('/html/body/app-root/app-root/main/dynamic-comp/div/div/div[1]/div/p/a[2]')
tab = link.get_attribute('outerHTML')
soup = BeautifulSoup(tab, 'html.parser')
sheet = soup.find(name='a').get('href')
sheet = sheet.split('/')
sheet = sheet[-1]

'''
if os.path.exists(f':C\Download\{sheet}') is True:
    modTimesinceEpoc = os.path.getmtime(f':C\Download\{sheet}')
    modificationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modTimesinceEpoc))
    print(modTimesinceEpoc - time.localtime())
    if (modTimesinceEpoc - time.localtime()) < 1500000:
        print('Arquivo recém-baixado!')
        pass
else:
    link.click()
'''