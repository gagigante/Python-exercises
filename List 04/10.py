# Faça um programa que leia uma lista com dez caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

vowels = ['a','e','i','o','u']
consonants = []
count = 0

for i in range(10):
  character = str(input('Digite um caracter: ')).lower() 

  if character in vowels:          
    pass
  else:
    consonants.append(character)
    count += 1

print(f'Foram inseridas {count} consoantes: {consonants}')