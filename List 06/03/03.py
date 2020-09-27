# Recriar o jogo da forca. Utilize sua criatividade, arquivos, funções, módulos, etc.
import random

def correctChoose(letter, word):
  hits = 0

  for i in word:
    if letter.lower() in i.lower():
      hits += 1
  return hits

def showGallow(word, errors, letras):
  letterExists = False  
  
  gallow = '|---------------|\n'

  if errors == 1:
    gallow += '|               O\n'
  elif errors == 2:
    gallow += '|              O\n'
    gallow += '|              |\n'
  elif errors == 3:
    gallow += '|              O\n'
    gallow += '|             /|\n'
  elif errors == 4:
    gallow += '|              O\n'
    gallow += '|             /|\\\n'
  elif errors == 5:
    gallow += '|              O\n'
    gallow += '|             /|\\\n'
    gallow += '|             /\n'
  elif errors == 6:
    gallow += '|              O\n'
    gallow += '|             /|\\\n'
    gallow += '|             /\\\n'

  gallow += '|\n' * 4
  gallow += '|   '

  for i in word:
    for letter in correctAttempts:
      if letter in i.lower():
        gallow += letter.lower() + ' '
        letterExists = True
    if(not letterExists):
      gallow += '_ '  
    letterExists = False       
  
  return gallow

programmingLanguages = ['java', 'csharp', 'python', 'javascript', 'elixir', 'php', 'go', 'dart','c', 'typescript']

selectedLanguage = random.choice(programmingLanguages)

correctAttempts = []
attempts = []

gallow = showGallow(selectedLanguage, 0, correctAttempts)

print(selectedLanguage)
print(gallow)

hits = 0
errors = 0

while True:
  if(errors == 6):
    print('Suas tentativas acabaram')
    break

  choose = input('\n\nDigite uma letra: ')
  
  if choose in attempts or choose in correctAttempts:
    print('Você já escolheu essa opção')
  else:
    hit = correctChoose(choose, selectedLanguage)

    if hit > 0:
      hits += hit
      correctAttempts.append(choose)
    else:
      errors += 1        
      attempts.append(choose) 
    
    gallow = showGallow(selectedLanguage, errors, correctAttempts)
    
    print(gallow)
    print('Letras erradas: ', end = '')
    print(attempts)

    if hits == len(selectedLanguage):
      print('Você venceu')
      break