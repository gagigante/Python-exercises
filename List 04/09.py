# Elabore um programa que efetue a leitura de quatro notas reais, adicione-as a 
# uma lista e mostre-as, inclusive a média aritmética, arredondar duas casas 
# decimais. Verifique e exiba as devidas mensagens se o aluno está aprovado ou 
# não, considerando que a média de aprovação é maior ou igual a 7.0, e em 
# prova exame, se média aritmética entre 4.0 e menor que 7.0. E reprovado, se menor que 4.0.

data = []
total = 0

for i in range(4):
    num = float(input('Digite uma nota: '))

    data.append(num)
    total += num

avg = round(total / 4, 2)

print(f'Suas notas são {data} e sua média é {avg}')

if avg >= 7:
  print('Você está aprovado')
elif avg >= 4 and avg < 7:
  print('Exame de recuperação')
else:
  print('Reprovado')