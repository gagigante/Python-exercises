# Elaborar um programa que receba uma medida em pés e apresente o valor convertido em metros.

footValue = float(input('Informe um valor em pés ').replace(',', '.'))

print(f'O valor em metros é {footValue * 0.3048}')