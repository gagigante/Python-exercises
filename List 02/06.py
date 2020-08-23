# Faça um programa para calcular e exibir o desconto na compra do cliente, conforme o valor da compra do mesmo digitado pelo usuário (incluindo centavos – cuidado com o uso do tipo de dados correto)

valor = float(input('Digite o valor da compra ').replace(',', '.'))

if valor <= 50.00:
  valor = valor * 0.05
elif 100.00 >= valor > 50.00:
  valor = valor * 0.08
elif 150.00 >= valor > 100.00:
  valor = valor * 0.12
else:
  valor = valor * 0.15

print(f'O valor do desconto é {value}')