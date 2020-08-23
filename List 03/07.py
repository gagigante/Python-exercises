# Faça um programa que apresente os resultados da soma e da média aritmética dos valores pares situados na faixa numérica de 50 a 70

print()

total = qtt = 0
   
for i in range(50, 71):
  total += i
  qtt += 1

media = total / qtt

print(f'A média é {media}')