# Faça um algoritmo que apresente todos os valores numéricos divisíveis por 4 e menores que 200.

i = 1

while i <= 200:
  if i % 4 == 0:
    print(i)
  i += 1
