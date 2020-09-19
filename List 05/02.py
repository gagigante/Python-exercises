# Questão 1. Elabore um programa que imprima um número por linha até atingir o número 
# informado pelo usuário. Use uma função que receba um número inteiro informado pelo usuário e 
# imprima até a n-ésima linha.

def printNumber(number):
  for x in range(1, number + 1):
    numberFor = x
    
    for y in range(x):
      print(numberFor)

number = int(input('Digite um número: '))

printNumber(number)