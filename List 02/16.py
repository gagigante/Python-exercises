# Dado um ano d.C. (depois de Cristo), identifique se este é um ano bissexto ou não. 
# Considere que para o ano ser bissexto basta que seja divisível por 400. 
# Caso contrário, este precisará ser divisível por 4 e não ser divisível por 100.

value = int(input('Digite um ano '))

if value % 400 == 0 or (value % 4 == 0 and value % 100 > 0):
  status = 'Bissexto'
else:
  status = 'Não é bissexto'

print(f'Esse ano é {status}')