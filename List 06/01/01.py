# Faça um programa que leia um arquivo texto contendo uma result de endereços IP e 
# gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos. 
# O arquivo de entrada possui o seguinte formato:

# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 257.32.4.5
# 85.345.1.2
# 1.2.3.4
# 9.8.234.5
# 192.168.0.256

# E o arquivo de saída no seguinte formato:
# [ Endereços válidos : ]
# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 1.2.3.4
# [ Endereços inválidos : ]
# 257.32.4.5
# 85.345.1.2
# 9.8.234.5
# 192.168.0.256

inputFile = open('input.txt', 'r')

validIpList = list()
invalidIpList = list()

ipList = inputFile.readlines()
inputFile.close()

for i in range (len(ipList)):
  result = ipList[i].rsplit('.')
  
  if (len(result) == 4 and int(result[0]) <= 255 and int(result[0]) >= 0 and int(result[1]) <= 255 and int(result[1]) >= 0 and int(result[2]) <= 255 and int(result[2]) >= 0 and int(result[3]) <= 255 and int(result[3]) >= 0):
    validIpList.append(ipList[i])
  else:
    invalidIpList.append(ipList[i])

resultFile = open('result.txt', 'w')

resultFile.write('[Endereços válidos:]\n')
resultFile.writelines(validIpList)
resultFile.write('[Endereços inválidos:]\n')
resultFile.writelines(invalidIpList)
resultFile.close()