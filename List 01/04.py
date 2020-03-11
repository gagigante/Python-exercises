salary = float(input('Informe o salário base: '))

earns = (salary / 100) * 5
spends = (salary / 100) * 7

finalSalary = salary + earns - spends

print(f'Após pagar 7% {spends} sobre o salário base em impostos e ganhar 5% {earns} sobre o salário base em gratificação o resultado será {finalSalary}')
