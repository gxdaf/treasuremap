import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456",
  database = "treasuremap"
)

cursor = db.cursor()

#cursor.execute('CREATE DATABASE treasuremap')

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
    com = []
    for celula in celulas:
      com.append(f'INSERT INTO {tabela} {celula};')
    #for i in range(len(com)):
     # pass
  except:
    pass