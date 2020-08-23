# Faça um programa que apresente todos os valores numéricos inteiros ímpares situados na faixa de 0 a 2000.

i = 1

while i <= 2000:
  if i % 2 != 0:
    print(i)
  i += 1
