# Pedro comprou um saco de ração com peso em quilos. 
# Pedro possui dois gatos para os quais fornece a quantidade de ração em gramas. 
# Faça um programa que receba o peso do saco de ração e a quantidade de ração fornecida para cada gato. 
# Calcule e mostre quanto restará de ração no saco após cinco dias.

SackWeightInKg = float(input('Informe o peso do saco de ração em KG ').replace(',', '.'))
portionInGm = float(input('Informe a porção de ração para cada gato em gramas ').replace(',', '.'))

rest = SackWeightInKg * 1000 - (portionInGm * 2) * 5

print(f'Restará, após 5 dias, {rest} gramas de ração')
