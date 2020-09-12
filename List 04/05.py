# Faça um programa que leia um número de telefone, e corrija o número no 
# caso deste conter somente 7 dígitos, acrescentando o ’3’ na frente. 
# O usuário pode informar o número com ou sem o traço separador.

phone = input('Digite um número de telefone: ')

separator = False

for i in phone:
  if i == '-':
    separator = True

if len(phone) == 7 or len(phone) == 8 and separator:
  phone = '3' + phone 
  
print(f'Seu telefone é {phone}')