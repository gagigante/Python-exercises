# Elabore um programa que efetue a leitura de quinze números inteiros, 
# adicione-os a uma data e mostre-a de forma invertida, do último para o primeiro.

data = []
for i in range(15):
  data.append(int(input('Adicione um número: ')))  

print(data[::-1])