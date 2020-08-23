# Faça um programa que receba o valor do salário mínimo, e a quantidade de quilowatts 
# gasta por um consumidor e o tipo de consumidor (1-residencial, 2-comercial, 3-industrial) e que calcule e mostre:

# O valor de cada quilowatt, sabendo que o quilowatt custa um oitavo do salário mínimo.
# O valor a ser pago por consumidor (conta final mais o acréscimo).
# O faturamento geral da empresa,
# A quantidade de consumidores que pagam entre 500,00 e 1000,00.
# Terminar a entrada de dados ao digitar uma quantidade de quilowatt igual a zero.
# O acréscimo encontra-se na tabela a seguir:

revenues = 0
consumers = 0

while True: 
  kwQtt = int(input('Informe a quantidade de KW '))
  
  if kwQtt == 0:
    break
  
  minimunWage = float(input('Informe o salário mínimo ').replace(',', '.'))
  consumerType = int(input('Informe seu tipo de consumo: (1-residencial, 2-comercial, 3-industrial)'))

  kwValue = minimunWage / 8
  value = kwQtt * kwValue

  if consumerType == 1:
    valueToBePaid = value + (value * 0.05)
  elif consumerType == 2:
    valueToBePaid = value + (value * 0.1)
  else:
    valueToBePaid = value + (value * 0.15)

  revenues += valueToBePaid

  if 500 <= valueToBePaid <= 1000:
    consumers += 1

  print(f'O valor de cada QuiloWatt é {kwValue}')
  print(f'O valor pago do consumidor é {valueToBePaid}')

print(f'O faturamento total da empresa é {revenues}')
print(f'A quantidade de consumidores que pagam entre R$ 500,00 e R$ 1000,00 é {consumers}')

  