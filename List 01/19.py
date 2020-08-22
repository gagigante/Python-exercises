# Efetuar o cálculo e apresentar o valor de uma prestação de um bem em atraso, utilizando a fórmula:
# prestacao = valor + (valor (taxa / 100) tempo)

value = float(input('Digite o valor da prestação ').replace(',', '.'))
rate = float(input('Digite o valor da taxa ').replace(',', '.'))
days = int(input('Digite o tempo de atraso em dias '))

installment =  value + (value * (rate / 100) * days)

print(f'Valor da prestação, com {days} dias de atraso, é {installment}')