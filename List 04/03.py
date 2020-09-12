# Elaborar um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e indique se é um 
# número válido ou inválido através da validação dos dígitos verificadores e dos caracteres de formatação

cpf = input('Digite seu CPF: ')

if len(cpf) == 14 and cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-':
  print('CPF é válido')
else:
  print('CPF não é válido')