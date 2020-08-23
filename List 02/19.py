# Efetuar a leitura de um valor numérico inteiro positivo ou negativo representado pela variável 
# N e apresentar o valor lido como sendo positivo. Dica: se o valor lido for menor que zero, 
# o mesmo deve ser multiplicado por -1.

number = int(input('Digite um valor '))

if number < 0:
  number = number * -1

print(f'O resultado é {number}')