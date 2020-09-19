# Questão 8. Elabore um programa que utilize uma função que informe a 
# quantidade de dígitos de um determinado número inteiro informado.

def numberOfDigits(number):
  print(len(str(number)))

number = int(input('Digite um número: '))
numberOfDigits(number)