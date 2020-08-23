# Faça um programa que simule uma calculadora com as quatro operações básicas (+, -, *, / ). 
# O programa deve solicitar ao usuário a entrada de dois operandos e da operação a ser executada, 
# na forma de menu. Dependendo da opção escolhida, deve ser executada a operação solicitada e escrito seu resultado. 
# Utilize uma variável do tipo inteiro para armazenar a operação e utilize o comando caso
#  para escolher a operação a ser executada a partir do operador.

value1 = int(input('Digite um número '))
value2 = int(input('Digite outro número '))
operation = input('Escreva a operação ')

if operation == 'Multiplicação':
  value = value1 * value2
elif operation == 'Soma':
  value = value1 + value2
elif operation == 'Subtração':
  value = value1 - value2
elif operation == 'Divisão':
  value = value1 / value2
else:
  value = 'Operação não reconhecida'

print(f'O resultado é {value}')