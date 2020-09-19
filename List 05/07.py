# Questão 7. Elabore um programa que utilize uma função com o nome valor_pagamento 
# para determinar o valor a ser pago por uma prestação de uma conta. O programa 
# deverá solicitar ao usuário o valor da prestação e o número de dias em atraso 
# e passar estes valores para a função valorPagamento, que calculará o valor a 
# ser pago e devolverá este valor ao programa que a chamou. O programa deverá 
# então exibir o valor a ser pago na tela. Após a execução o programa deverá 
# voltar a pedir outro valor de prestação e assim continuar até que seja informado 
# um valor igual a zero para a prestação. Neste momento o programa deverá ser 
# encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total 
# de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. 
# Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, 
# cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

def valor_pagamento(value, days): 
  if(days > 0):
    return value * 1.03 + 0.001 * days
  
  return valor

total = qtt = 0

while True:
  value = float(input('Valor da prestação: '))

  if value == 0:
    print(f'A quantidade de prestações pagas foram {qtt} com um total de R${round(total, 2)}')
    break
    
  days = int(input('Dias em atraso: '))

  print(f'Valor a ser pago {round(valor_pagamento(value, days), 2)}')

  qtt += 1
  
  total += valor_pagamento(value, days)