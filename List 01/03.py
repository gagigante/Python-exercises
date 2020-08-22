# Faça um programa que receba o salário de um funcionário e o percentual de aumento, calcule e mostre o valor do aumento e o novo salário.

salary = float(input('Informe seu salário: ').replace(',', '.'))
increasePercent = float(input('Informe a porcentagem de aumento: ').replace(',', '.'))

increasedSalary = salary + (salary/100) * increasePercent

print(f'O salario aumentado em {increasePercent}% é {increasedSalary}')
