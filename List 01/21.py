# Escreva um programa que solicite ao usuário dois números e apresente na tela os resultados das operações aritméticas (soma, subtração, multiplicação, divisão, resto da divisão, exponenciação, radiciação).

number1 = int(input('Informe o primeiro número '))
number2 = int(input('Informe o segundo número '))

print(f'Soma: {number1 + number2}')
print(f'Subtração: {number1 - number2}')
print(f'Multiplicação: {number1 * number2}')
print(f'Divisão: {number1 / number2}')
print(f'Resto da divisão: {number1 % number2}')
print(f'Exponenciação: {number1 ** number2}')
print(f'Radiciação: {number1 ** (1 / number2)}')