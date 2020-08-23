# Faça um programa para calcular e exibir a valor do imposto de ICMS de um produto, conforme a classificação do tipo de produto e do valor de custo do mesmo digitado pelo usuário (incluindo centavos – cuidado com o uso do tipo de dados correto).

value = float(input('Digite o valor do produto ').replace(',', '.'))
productType = input('Digite o tipo do produto (Cesta Básica, Eletrônicos ou Serviços)')

if productType == 'Cesta Básica':
  value = 0
elif productType == 'Eletrônicos':
  value = value * 0.25
elif productType == 'Serviços':
  value = value * 0.18
else:
  value = value * 0.12

print(f'O valor do imposto é {value}')