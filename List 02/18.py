# Efetuar a leitura de dois valores numéricos inteiros representados pelas variáveis A e B e 
# apresentar o resultado da diferença do maior valor pelo menor

a = int(input('Digite um número '))
b = int(input('Digite outro número '))

if a > b:
  result = a - b 
else:
  result = b - a
  
print(f'O resultado é {result}')