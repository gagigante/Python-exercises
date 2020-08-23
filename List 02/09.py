# Faça um programa para calcular e exibir o desconto na compra do cliente em uma farmácia, conforme o valor da compra do mesmo digitado pelo usuário (incluindo centavos – cuidado com o uso do tipo de dados correto)

value = float(input('Digite o valor total de serviços ').replace(',', '.'))

if value <= 150.00:
  value = value * 0.05
elif 300.00 >= valor > 150.00:
  value = value * 0.07
elif 500.00 >= value > 300.00:
  value = value * 0.10
else:
  value = value * 0.20

print(f'O valor do desconto é {value}')