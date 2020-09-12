# Elabore um programa que efetue a leitura de cinco números inteiros, adicione-os a uma data e mostre-a.

data = []

for i in range(5):
  data.append(int(input('Adicione um número: ')))  
      
print(data)