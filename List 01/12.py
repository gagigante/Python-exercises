# Criar um programa que efetue o cálculo da hora aula líquida 
# (descontado o percentual de imposto) de um professor. 
# Os dados fornecidos serão: valor da hora aula, número de aulas dadas no 
# mês e percentual de desconto do INSS.
 
value = float(input('Digite o valor do salário mínimo ').replace(',', '.'))
classesPerMonth = float(input('Digite o número de aulas dadas no mês ').replace(',', '.'))
inss = float(input('Digite o percentual de desconto do INSS '))

netValue = (value * classesPerMonth) - ((value * classesPerMonth) * (inss / 100))

print(f'O valor líquido que irá receber é {netValue}')