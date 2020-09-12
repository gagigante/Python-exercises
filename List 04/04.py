# Elaborar um programa que a partir da digitação de uma frase, o programa 
# informe quantos espaços em branco e quantos são, e quantas vezes aparecem cada uma das vogais a, e, i, o, u.

phrase = input('Digite uma frase: ').lower()

vowels = { 'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0, ' ': 0 }

for i in phrase:
  if i in vowels:
    vowels[i] += 1

print(vowels)