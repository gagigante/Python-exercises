# Elaborar um programa que calcule e apresente em metros por segundo o valor da velocidade de um projétil que percorre uma distância em quilômetros a um espaço de tempo em minutos.

distance = float(input('Informe a distância percorrida em KM ').replace(',', '.'))
time = int(input('Informa o tempo em minutos '))

distanceInMeters = distance * 1000
timeInSeconds = time * 60

print(f'A valocidade do projétil que se desloca {distance} KM em {time} minutos é {distanceInMeters / timeInSeconds} m/s')