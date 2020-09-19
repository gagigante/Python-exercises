# Questão 3. Elabore um programa que utilize uma função que solicite 
# três argumentos, e que forneça a soma desses três argumentos.

def sumNumbers(x, y, z):
  return print(f'A soma é {x + y + z}')

x = int(input('Digite um número: '))
y = int(input('Digite um número: '))
z = int(input('Digite um número: '))

sumNumbers(x, y, z)