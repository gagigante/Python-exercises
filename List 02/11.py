# Faça um programa que leia um número inteiro e diga se este é positivo, negativo ou zero

value = int(input('Digite um número '))

if valor < 0:
  status = 'Negativo'
elif valor == 0:
  status = 'Zero'
else:
  status = 'Positivo'

print(f'Esse número é {status}')