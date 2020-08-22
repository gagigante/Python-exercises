# Faça um programa que receba três notas, calcule e mostre a média aritmética entre elas. Exiba, as notas, e a respectiva média.

grade01 = float(input('Informe a primeira nota: '))
grade02 = float(input('Informe a segunda nota: '))
grade03 = float(input('Informe a terceira nota: '))

average = (grade01 + grade02 + grade03) / 3

print(f'Nota 01: {grade01}; Nota 01: {grade02}; Nota 03: {grade03}')
print(f'Média: {average}')
