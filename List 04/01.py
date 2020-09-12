# Elabore um programa que efetue a leitura de duas strings e informe o seu conteúdo, 
# seguido de seu comprimento. Indique também se as duas strings possuem o mesmo 
# comprimento e se são iguais ou diferentes no conteúdo.

data = {}

for i in range(2):
  word = input('Digite uma word: ')
  data[i] = [word, len(word)]

print(data)

if data[0][0] == data[1][0]:
  print('São iguais')
if data[0][1] == data[1][1]:
  print('Possuem o mesmo comprimento')