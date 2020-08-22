# Elabore um programa que calcule e exiba a média aritmética de 5 números ( k, x, y, z, w).

k = float(input('Informe o valor de k ').replace(',', '.'))
x = float(input('Informe o valor de x ').replace(',', '.'))
y = float(input('Informe o valor de y ').replace(',', '.'))
z = float(input('Informe o valor de z ').replace(',', '.'))
w = float(input('Informe o valor de w ').replace(',', '.'))

print(f'A média aritmética entre os números é {(k + x + y + z + w) / 5}')