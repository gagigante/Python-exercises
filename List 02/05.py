# Faça um programa para calcular e exibir a value do imposto de ISS de uma nota fiscal de serviços, conforme o value total de serviços especificado na mesma digitado pelo usuário (incluindo centavos – cuidado com o uso do tipo de dados correto).

value = float(input('Digite o value total de serviços ').replace(',', '.'))

if value <= 5000.00:
  value = value * 0.04
elif 10000.00 >= value > 5000.00:
  value = value * 0.06
elif 20000.00 >= value > 1000.00:
  value = value * 0.13
else:
  value = value * 0.16

print(f'Valor do imposto de ISS é {value}')