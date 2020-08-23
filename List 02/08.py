# Faça um programa para calcular e exibir a quantidade de parcelas sem juros e o valor de cada parcela, conforme o valor da compra digitado pelo usuário (incluindo centavos – cuidado com o uso do tipo de dados correto).

value = float(input('Digite o valor da compra ').replace(',', '.'))

if value <= 100.00:
  value = value / 2
  installments = 2
elif 200.00 >= value > 100.00:
  value = value / 3
  installments = 3
elif 400.00 >= value > 200.00:
  value = value / 4
  installments = 4
else:
  value = value / 5
  installments = 5

print(f'O valor das , {installments}, parcelas sem juros {value}')