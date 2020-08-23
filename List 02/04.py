# Faça um programa para calcular e exibir o desconto de IR conforme o valor do salário digitado pelo usuário (incluindo centavos – cuidado com o uso do tipo de dados correto).

value = float(input('Digite o salário '))

if value <= 1250.00:
  value = 0
elif 1900.00 >= value > 1250.00:
  value = value * 0.11
elif 2700.00 >= value > 1900.00:
  value = value * 0.25
else:
  value = value * 0.275

print(f'Valor do desconto de IR é {value}')