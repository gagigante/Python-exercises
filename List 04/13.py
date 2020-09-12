# Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de 
# modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses
# carros, isto é, quantos quilômetros cada um desses carros faz com um litro de 
# combustível. Calcule e mostre:

# - O modelo do carro mais econômico;
# - Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe 2,25 o litro.
# - Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa.
# - Relatório Final

# 1 - SUV - 10.0 - 100.0 litros - R 399.0
# 2 - IDEA - 12.0 - 83.3 litros - R 332.5
# 3 - GOL - 10.0 - 100.0 litros - R 399.0
# 4 - BMW - 20.0 - 50.0 litros - R 199.5
# 5 - UNO - 2.0 - 500.0 litros - R 1995.0
# O menor consumo é do BMW.

cars = ['Fusca', 'Gol', 'Vectra', 'Uno', 'Amarok']
consumption = [20.0,18.0,9.5,15.0,5.7]
mostEconomical = 0
counter = 0

for i in consumption:    
  print(f'{counter + 1} - {cars[counter]} - {i} - {round(1000 / i, 1)} litros - R$ {round(1000 / i *2.25, 1)}')
    
  if i < mostEconomical or mostEconomical == 0:
    mostEconomical = i
    carro = counter
    counter += 1

print(f'O menor consumo é do {cars[carro]}')