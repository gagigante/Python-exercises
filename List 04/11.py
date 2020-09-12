#  Faça um programa que leia 15 números inteiros e armazene-os em uma lista 
# NUMEROS. Armazene os números pares na lista PAR e os números ímpares na 
# lista IMPAR. Imprima os três vetores.

numbers = []
pair = []
odd = []

for i in range(15):
  number = int(input('Digite um número: '))

  numbers.append(number)      
  
  if number % 2 == 0:          
    pair.append(number)
  else:
    odd.append(number)

print(f'Os números digitados foram {numbers} dentre eles esses são pares {pair} e estes são ímpares {odd}')