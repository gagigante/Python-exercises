# Faça um programa para calcular e exibir a categoria do nadador, dado a sua idade.

age = int(input('Digite a sua idade '))

if 8 >age >= 5:
  category = 'Infantil A'
elif 10 >= age >= 8:
  category = 'Infantil B'
elif 13 >= age >= 11:
  category = 'Juvenil A'
elif age >= 14 and age < 17:
  category = 'Juvenil B'
else:
  category = 'Senior'

print(f'A categoria é {category}')