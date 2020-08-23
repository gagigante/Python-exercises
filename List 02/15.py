# Faça um programa que leia três valores que representam os lados de um triângulo. 
# Primeiramente, verifique se os lados podem formar um triângulo 
# ( a soma de dois lados não pode ser menor que o terceiro lado ). 
# Caso possa formar um triângulo, indique se este é equilátero, isósceles ou escaleno.

value1 = int(input('Digite um lado '))
value2 = int(input('Digite outro lado '))
value3 = int(input('Digite outro lado '))

if (value1 + value2) < value3 or (value1 + value3) < value2 or (value2 + value3) < value1:
  result = 'Não é um triângulo'
elif value1 == value2 and value1 == value3:
  result = 'Triângulo Equilátero'
elif (value1 == value2 and value1 != value3) or (value2 == value3 and value1 != value3) or (value1 == value3 and value2 != value3):
  result = 'Triângulo Isósceles'
else:
  resultado = 'Triângulo Escaleno'
  
print(f'O resultado é {result}')