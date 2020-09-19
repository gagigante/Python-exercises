# Faça um programa de implemente um jogo de Craps. O jogador 
# lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira 
# jogada, você tirar 7 ou 11, você um 'natural' e ganhou. Se você 
# tirar 2, 3 ou 12 na primeira jogada, isto é chamado de 'craps' e você perdeu. 
# Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10, este é seu 'Ponto'. 
# Seu objetivo agora é continuar jogando os dados até tirar este número novamente. 
# Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.

import random

def playDices():
  return random.randint(2, 12)

roundNumber = 0
score = 0

while True:
  roundNumber += 1

  if roundNumber > 1:
    print(f'O valor do ponto é {score}')
    
  value = playDices()

  print(f'O valor do dado é {value}')

  if roundNumber == 1:
    if value == 7 or value == 11:
      print('Tirou um natural, ganhou!')
      exit()
    elif value == 2 or value == 3 or value == 12:
      print('Tirou um Craps, perdeu!')
      exit()
    else:
      score = value
  else:
    if value == 7:
      print('Tirou um 7 antes, perdeu!')
      exit()
    elif score == value:
      print('Tirou seu ponto, ganhou!')
      exit()