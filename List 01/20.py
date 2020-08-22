# Escreva um programa que calcule e exiba na tela o perímetro e área de uma circunferência. 
# Dados: area = Pi raio ** 2, perimetro = 2 Pi * raio.

import math

radius = float(input('Informe o raio da circunferência ').replace(',', '.'))

area = math.pi * radius ** 2
perimeter = 2 * math.pi * radius

print(f'A área da circunferência é {area} e o perímetro é {perimeter}')