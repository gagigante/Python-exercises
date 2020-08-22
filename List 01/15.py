# Elabore um programa que permita a entrada de dois valores ( x, y ), troque seus valores entre si e então exiba os novos resultados.

x = int(input('Informe o valor de X '))
y = int(input('Informe o valor de Y '))

temp = 0

temp = x

x = y
y = temp

print(f'Os valores foram invertidos. X = {x} e Y = {y}')