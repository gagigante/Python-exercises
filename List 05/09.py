# Questão 9. Elabore um programa que utilize uma função que retorne 
# o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

def reverse(number):
  print(str(number)[::-1])

number = int(input('Digite um número: '))

reverse(number)