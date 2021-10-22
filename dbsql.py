import mysql.connector
from numpy import e
import time

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456",
  database = "treasuremap"
)

cursor = db.cursor(buffered = True)

#cursor.execute('CREATE DATABASE treasuremap')

def att_tab(tabela, celulas = None):
  print('1. Atualizar completamente (TRUNCATE);\n2. Atualizar valores já existentes (UPDATE/DELETE);\n3. Alterar tabela.')
  tipo_att = input('Escolha a opção: ')
  if '1' in tipo_att:
    try:
      cursor.execute(f'TRUNCATE TABLE {tabela}')
      cursor.commit()
      ins_tab(tabela, celulas)
    except Exception as E:
      raise e
  else:
    pass

def cr_tab(tabela, colunas, tipo):
  try:
    cursor.execute(f'SELECT * FROM {tabela}')
    pass
  except:
    for i in range(len(colunas)):
      if i == 0:
        com = f'{colunas[i]} {tipo[i]}, ' 
      elif i == (len(colunas) - 1):
        com += f'{colunas[i]} {tipo[i]}' 
      else:
        com += f'{colunas[i]} {tipo[i]}, ' 
    query = f'CREATE TABLE {tabela}({com});'
    cursor.execute(query)

def drop_tab(tabela):
  try:
    cursor.execute(f'DROP TABLE {tabela};')
  except:
    print(f'{tabela} não existe.')

def ins_tab(tabela, celulas):
  try:
    cursor.execute(f'SELECT * FROM {tabela}')
    cursor.execute(f'SHOW COLUMNS FROM {tabela}')
    for x in cursor:
      print(x[0])
    colunas = input('Escreva a ordem do INSERT')
    for celula in celulas:
      for c in range(len(celula)):
        if c == 0:
          com = f'{celula[c]}, '
        elif c == (len(celula) - 1):
          com += f'{celula[c]}'
        else:
          com += f'{celula[c]}, '
      query = f"INSERT INTO {tabela} ({colunas}) VALUES ({com});"
      print(query)
      try:
        cursor.execute(query)
        db.commit()
      except Exception as e:
        raise e
      time.sleep(2)
  except Exception as e:
    raise e