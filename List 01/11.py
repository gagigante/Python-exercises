# Antes de o racionamento de energia ser decretado, quase ninguém falava em quilowatts; 
# mas, agora, todos incorporam essa palavra em seu vocabulário. 
# Sabendo-se que 100 quilowatts de energia custa um sétimo 
# do salário mínimo, fazer um programa que receba 
# o valor do salário mínimo e a quantidade de quilowatts gasta por uma residência
#  e calcule. Imprima:

# o valor em reais de cada quilowatt,
# o valor em reais a ser pago,
# o novo valor a ser pago por essa residência com um desconto de 10%

minimumWage = float(input('Digite o valor do salário mínimo ').replace(',', '.'))
totalKw = float(input('Digite a quantidade de quilowatt ').replace(',', '.'))

kwValue = minimumWage / 7
amountPaid = kwValue * totalKw
discount = amountPaid - (amountPaid * 0.1)

print(f'Valor de cada kw é {kwValue}, o valor pago é {amountPaid} e o valor pago descontado é {discount}')