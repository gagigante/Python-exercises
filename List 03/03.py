# Faça um programa que receba o número sorteado por um dado em vinte jogadas. 
# Exibir os números sorteados e a frequência com que cada um aparece.


timesOneWasDrawn = timesTwoWasDrawn = timesThreeWasDrawn = timesFourWasDrawn = timesFiveWasDrawn = timesSixWasDrawn = 0

for i in range(20):
  drawn = int(input('Informe o número sorteado '))

  if drawn == 1:
    timesOneWasDrawn += 1
  elif drawn == 2:
    timesTwoWasDrawn += 1
  elif drawn == 3:
    timesThreeWasDrawn += 1
  elif drawn == 4:
    timesFourWasDrawn += 1
  elif drawn == 5:
    timesFiveWasDrawn += 1
  elif drawn == 6:
    timesSixWasDrawn += 1

print(f'Um = {timesOneWasDrawn}, Dois = {timesTwoWasDrawn}, Três = {timesThreeWasDrawn}, Quatro = {timesFourWasDrawn}, Cinco = {timesFiveWasDrawn}, Seis = {timesSixWasDrawn}')

