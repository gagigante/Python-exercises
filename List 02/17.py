# Faça um programa que calcule o IMC de uma pessoa (IMC = massa em kg / altura em metros elevado ao quadrado) e informe a sua classificação

mass = float(input('Digite a sua massa ').replace(',', '.'))
height = float(input('Digite a sua altura ').replace(',', '.'))

imc = mass / (height * height)

if imc < 17.00:
  status = 'Muito abaixo do peso'
elif 18.50 >= imc >= 17.00:
  status = 'Abaixo do peso'
elif 25.00 >= imc >= 18.50:
  status = 'Peso normal'
elif 30.00 >= imc >= 25.00:
  status = 'Acima do peso'
elif 35.00 >= imc >= 30.00:
  status = 'Obesidade I'
elif 40.00 >= imc >= 35.00:
  status = 'Obesidade II'
else:
  status = 'Obesidade III (mórbida)'

print(f'Sua classificação é {status}')