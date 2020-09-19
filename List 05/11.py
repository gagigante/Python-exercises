# Questão 11. Construa uma função que receba uma data no formato DD/MM/AAAA 
# e devolva uma string no formato D de mes_por_extenso de AAAA. Opcionalmente, 
# valide a data e retorne NULL caso a data seja inválida. (Pesquisar sobre 
# expressão regular para resolver a questão para validar o texto por extenso.)

import re

def fullMonth(date):
  fullMonth = {
    1: 'janeiro', 
    2: 'fevereiro', 
    3: 'março', 
    4: 'abril',
    5: 'maio',
    6: 'junho',
    7: 'julho',
    8: 'agosto',
    9: 'setembro',
    10: 'outubro',
    11: 'novembro',
    12: 'dezembro',
  }

  regexMatch = re.search('\d{2}/\d{2}/\d{4}', date)

  if regexMatch:
    day, month, year = date.split('/')

    print(f'{day} de {fullMonth[int(month)]} de {year}')
  else:
    print('Não esta em formato DD/MM/AAAA')
        
date = input('Data em formato DD/MM/AAAA: ')

fullMonth(date)