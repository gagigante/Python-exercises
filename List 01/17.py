# Elabore um programa que calcule e exiba quantas notas de 50, 10 e 1 são necessárias para se pagar uma conta cujo valor é fornecido.

value = int(input('Informe um valor '))

remaining = 0

fiftyQtt = 0
tenQtt = 0
oneQtt = 0

if value >= 50:
  fiftyQtt = value // 50
  remaining = value % 50

if remaining >= 10:
  tenQtt = remaining // 10
  remaining = remaining % 10

if remaining >= 1:
  oneQtt = remaining / 1

print(f'R$50 = {fiftyQtt}, R$10 = {tenQtt}, R$1 = {oneQtt}')