# Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será 
# mostrada com as letras embaralhadas. O programa terá uma lista de palavras 
# lidas de uma lista a ser fixada inicialmente pelo programador e escolherá uma 
# aleatoriamente. O jogador terá uma única tentativa para adivinhar a palavra. 
# Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou 
# ou perdeu o jogo. Observação: Refaça, possibilitando ao jogador tentar até 5 vezes.

import random

words = ['são Paulo', 'corinthians', 'palmeiras', 'paisandu', 'santos', 'bragantino']

chosenWord = random.choice(words)

shuffled = list(chosenWord)
random.shuffle(shuffled)
shuffled = ''.join(shuffled)

userTry = input(f'Adivinhe a palavra {shuffled}: \n')

if chosenWord == userTry.lower():
  print('Você acertou')
else:
  print('Você errou')

print(f'A palavra era {chosenWord}')