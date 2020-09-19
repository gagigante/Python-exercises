# Questão 14. Elabore um programa que: Um quadrado mágico é aquele dividido 
# em linhas e colunas, com um número em cada posição e no qual a soma das linhas, 
# colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, 
# com números de 1 a 9:

import random
                
cube = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

isValid = True

def magicSquare():
  global isValid

  if cube[0][0] + cube[0][1] + cube[0][2] == cube[1][0] + cube[1][1] + cube[1][2] == cube[2][0] + cube[2][1] + cube[2][2] == cube[0][0] + cube[1][0] + cube[2][0] == cube[0][1] + cube[1][1] + cube[2][1] == cube[0][2] + cube[1][2] + cube[2][2] == cube[0][0] + cube[1][1] + cube[2][2]:
    isValid = False
 
while isValid:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in range(3):
      for j in range(3):
        number = random.choice(numbers)

        cube[i][j] = number

        numbers.remove(number)

    magicSquare()
    
print(cube[0][0], cube[1][0], cube[2][0])
print(cube[0][1], cube[1][1], cube[2][1])
print(cube[0][2], cube[1][2], cube[2][2])