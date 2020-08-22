# Faça um programa que receba o número de horas trabalhadas e o valor do salário mínimo. 
# Calcule e mostre o salário a receber seguindo as regras abaixo:

# a hora trabalhada vale a metade do salário mínimo;
# o salário bruto equivale ao número de horas trabalhadas multiplicado pelo valor da hora trabalhada;
# o imposto equivale a 3% do salário bruto;
# o salário a receber equivale ao salário bruto menos o imposto.

hours = int(input('Informe a quantidade de horas trabalhadas '))
salary = float(input('Informe seu salário mínimo ').replace(',', '.'))

hourValue = salary / 2
grossSalary = hourValue * hours
tax = grossSalary * 0.03

print(f'O salário a receber é {grossSalary - tax}')