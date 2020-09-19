# Questão 13. Construa uma função que desenhe um retângulo usando os 
# caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, 
# linhas e colunas, sendo que o valor por omissão é o valor mínimo 
# igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, 
# eles devem ser modificados para valores dentro da faixa de forma elegante.

def rectangle(width, height):
  if width > 20:
    width = 20
  elif width <= 0:
    width = 1
  if height > 20:
    height = 20
  elif height <= 0:
    height = 1

  print('-+-' * width)
  z = '|'
  for i in range(height):
    print('|', ' ' * (width * 3 - 4), '|')
    
  print('-+-' * width)

width = int(input('Digite a largura: '))
height = int(input('Digite a altura: '))

rectangle(width, height)