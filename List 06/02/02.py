# A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no 
# seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber 
# qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de 
# um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado 'userss.txt':

# alexandre 456123789
# anderson 1245698456
# antonio 123456456
# carlos 91257581
# cesar 987458
# rosemary 789456125

# Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa 
# que gere um relatório, chamado 'relatório.txt', no seguinte formato:

# O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, 
# de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes 
# deverá ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do 
# percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.

def convert(number):
  number = number / 1024
  number = number / 1024
  
  return number

def percent(list, number):   
  number = float(number) * 100
  number = number / sum(list)
  
  return number

inputFile = open('users.txt', 'r')

listItems = inputFile.readlines()
inputFile.close()

report = 'ACME Inc.  Uso do espaço em disco pelos usuários\n'
report += '-------------------------------------------------------\n'
report += 'Nr.\tUsuário\t\tEspaço utilizado\t % do uso\n'

users = []
space = []
percentual = []
sumNum = 0

for num in listItems:
  sumNum += (float(num[14:]))

for i in listItems:
  users.append(i[0:14])
  num = convert(int(i[14:]))
  space.append(num)

for i in range (len(users)):
  percentualNum = percent(space, space[i])
  percentual.append(percentualNum)

  report += str(i+1) + '\t'
  report += users[i] + '\t'
  report += str(round((space[i]), 2)) + '\tMB' + '\t\t'
  report += str(round((percentual[i]), 2)) + '\n'

result = open('report.txt', 'w')
result.writelines(report)