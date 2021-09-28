from os import name
import time
import requests
import datetime
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox import options
from selenium.webdriver.firefox.options import Options
import json

option = Options()
option.headless = True
driver = webdriver.Firefox()

url_se = 'https://www3.bcb.gov.br/expectativas2/#/consultaSeriesEstatisticas'
driver.get(url_se)

c = {0: ['/html/body/app-root/div/app-main/main/div/app-consulta-serie-estatisticas/section/div[2]/div[2]/div/div[2]/div[1]/input-ngselect/div/ng-select/div/div/div[2]/input', 'taxas', '/html/body/ng-dropdown-panel/div/div[2]/div/span'],
    1: ['/html/body/app-root/div/app-main/main/div/app-consulta-serie-estatisticas/section/div[2]/div[2]/div/div[2]/div[2]/input-ngselect/div/ng-select/div/div/div[2]/input', 'mensal','/html/body/ng-dropdown-panel/div/div[2]/div/span'],
    2: ['/html/body/app-root/div/app-main/main/div/app-consulta-serie-estatisticas/section/div[2]/div[2]/div/div[2]/div[3]/div[1]/input-ngselect/div/ng-select/div/div/div[2]/input', 'selic', '/html/body/ng-dropdown-panel/div/div[2]/div/span']}

time.sleep(5)

for k in range(3):
        x = driver.find_element_by_xpath(c.get(k)[0])
        x.click()
        time.sleep(1)
        x.send_keys(c.get(k)[1])
        time.sleep(1)
        x.find_element_by_xpath(c.get(k)[2]).click()
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

'''
url_sa = 'https://www.bcb.gov.br/controleinflacao/historicotaxasjuros'
driver.get(url_sa)
time.sleep(2)
xpath_sa = driver.find_element_by_xpath('//*[@id="historicotaxasjuros"]')
xpath_sa = xpath.get_attribute('outerHTML')
soup = BeautifulSoup(xpath_sa, 'html.parser')
selic = soup.find_all('td')[4].get_text()
taxas = {}
taxas['selic']['atual'] = selic
taxas['selic']['especulacao'] = 
print(atual)
#dados = open('dados.json', 'w')
'''