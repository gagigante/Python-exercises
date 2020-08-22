# Faça um programa que receba um número positivo e maior que zero, calcule e mostre:

# O número digitado ao quadrado;
# O número digitado ao cubo;
# A raiz quadrada do número digitado;
# A raiz cúbica do número digitado;
# A soma do quadrado mais o cubo do número digitado;

import math

number = float(input('Informe um numero ').replace(',', '.'))

print(f'O número ao quadrado é {number ** 2}')
print(f'O número ao cubo é {number ** 3}')

squared = pow(number, 1/2)
cubed = pow(number, 1/3)

print(f'A raiz quadrada do número é {squared}')
print(f'A raiz cúbica do número é {cubed}')

print(f'A soma do quadrado do número mais o cubo do número é {squared + cubed}')