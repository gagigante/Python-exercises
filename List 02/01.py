# Faça um programa para calcular e exibir o desconto de INSS conforme o value do salário digitado pelo usuário (incluindo centavos – cuidado com o uso do tipo de dados correto).

value = float(input('Digite o salário mínimo ').replace(',', '.'))

if value <= 600.00:
  value = value - (value * 0.07)
elif 800.00 >= value > 600.00:
  value = value - (value * 0.09)
elif 1200.00 >= value > 800.00:
  value = value - (value * 0.09)
else:
  value = value - (value * 0.11)

print(f'O valor líquido que irá receber é {value}')