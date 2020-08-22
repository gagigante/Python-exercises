# Um trabalhador recebeu seu salário e o depositou em sua conta corrente bancária. 
# Esse trabalhador emitiu dois cheques e agora deseja saber seu saldo atual. 
# Sabe-se que cada operação bancária de retirada paga CPMF de 0,38% e 
# o saldo inicial da conta está zerado.

deposit01 = float(input('Informe o valor do salário a ser depositado ').replace(',', '.'))
deposit02 = float(input('Informe o valor do salário a ser depositado ').replace(',', '.'))

balance = (deposit01 - deposit01 * 0.038) + (deposit02 - deposit02 * 0.038)

print(f'O saldo final é {balance}')