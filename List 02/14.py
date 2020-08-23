# Faça um programa que leia as repostas de três questões de múltipla escolha (a, b, c, d). 
# Em seguida, leia o gabarito dessas questões, ou seja, as respostas corretas. Depois, 
# compare as respostas dadas com as do gabarito e indique quantas respostas estão corretas

value1 = input('Raíz de 49 é\n a - 7\n b - 8\n c - 4\n d - 5\n')
value2 = input('\n3 vezes 7 é\n a - 27\n b - 21\n c - 26\n d - 22\n')
value3 = input('\nMelhor time de fut\n a - Bahia\n b - Paisandu\n c - Real madrid\n d - Fortaleza\n')

result = 0

if value1 == 'a':
    result = result + 1
if value2 == 'b':
    result = result + 1
if value3 == 'a':
  result = result + 1

print(f'Você acertou {result} questões')