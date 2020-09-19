# Questão 5. Elabore um programa que utilize uma função chamada soma_imposto. 
# A função possui dois parâmetros formais: taxaImposto, que é a quantia de 
# imposto sobre vendas expressa em porcentagem e custo, que é o custo de um 
# item antes do imposto. A função “altera” o valor de custo para incluir o imposto 
# sobre vendas.

def soma_imposto(tax, cost):
  return cost + (tax / 100 * cost)

tax = int(input('Imposto sobre vendas expressa em porcentagem: '))
cost = float(input('Custo do produto: '))

print(f'O custo com o imposto é {soma_imposto(tax, cost)}')