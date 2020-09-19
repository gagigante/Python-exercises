# Questão 4. Elabore um programa que utilize uma função que necessite de um 
# argumento. A função retorna o valor de caractere ‘P’, se seu argumento 
# for positivo, e ‘N’, se seu argumento for zero ou negativo.

def check(number):
  if number > 0:
    return print('P')

  return print('N')

number = int(input('Digite um número: '))

check(number)