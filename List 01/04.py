# Faça um programa que receba o salário-base de um funcionário, calcule e mostre o salário a receber, sabendo-se que esse funcionário tem gratificação de 5% sobre o salário-base e paga imposto de 7% sobre salário-base.

salary = float(input('Informe o salário base: ').replace(',', '.'))

earns = (salary / 100) * 5
spends = (salary / 100) * 7

finalSalary = salary + earns - spends

print(f'Após pagar 7% {spends} sobre o salário base em impostos e ganhar 5% {earns} sobre o salário base em gratificação o resultado será {finalSalary}')
