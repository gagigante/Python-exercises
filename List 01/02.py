grade01 = float(input('Informe a nota 01: '))
weight01 = int(input('Informe o peso da nota 01: '))

grade02 = float(input('Informe a nota 02: '))
weight02 = int(input('Informe o peso da nota 02: '))

grade03 = float(input('Informe a nota 03: '))
weight03 = int(input('Informe o peso da nota 03: '))

totalWeight = weight01 + weight02 + weight03

average = (grade01*weight01 + grade02*weight02 + grade03*weight03) / totalWeight

print(f'A média ponderada é: {average}')
