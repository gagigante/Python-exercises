# Elabore um programa que solicite ao usuário, o seu nome e em seguida mostre o 
# seu nome de trás para frente utilizando somente letras maiúsculas.

name = input('Digite seu nome: ')

print(name[::-1].upper())