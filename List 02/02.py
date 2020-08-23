# Faça um programa para calcular e exibir a porcentagem de comissão de vendas de um vendedor, conforme o volume mensal de vendas do mesmo digitado pelo usuário (incluindo centavos – cuidado com o uso do tipo de dados correto).

salesValue = float(input('Digite o salesValue de vendas ').replace(',', '.'))

if salesValue <= 5000.00:
  salesValue = salesValue * 0.02
elif 10000.00 >= salesValue > 5000.00:
  salesValue = salesValue * 0.05
elif 15000.00 >= salesValue > 10000.00:
  salesValue = salesValue * 0.07
else:
  salesValue = salesValue * 0.09

print(f'O valor recebido de comissão é {salesValue}')