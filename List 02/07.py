# Faça um programa para calcular e exibir a valor dos juros de um empréstimo bancário, conforme o valor emprestado e o número de parcelas digitado pelo usuário (incluindo centavos – cuidado com o uso do tipo de dados correto).

value = float(input('Digite o valor do empréstimo ').replace(',', '.'))
installmentQtt = int(input('Digite a quantidade de parcelas '))

if installmentQtt <= 3:
  value = value * 0.06
elif 6 >= installmentQtt > 3:
  value = value * 0.09
elif 12 >= installmentQtt > 6:
  value = value * 0.22
else:
  value = value * 0.34

print(f'O valor do juros é {value}')