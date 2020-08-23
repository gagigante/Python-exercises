# Faça um programa que leia valores positivos inteiros até que um valor negativo seja informado. Ao final devem ser apresentados o major e o menor valores informados pelo usuário. 

major = minor = i = 0

while True:
  value = int(input('Insira um valor '))

  if value < 0:
    break

  if i == 0:
    major = value
    minor = value
  elif value > major:
    major = value
  elif value < minor:
      minor = value
  i +=1

print(f'O maior valor é {major}, o menor valor é {minor} e o número de valores lidos é {i}')
    