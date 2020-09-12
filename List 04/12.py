# Elabore um programa que efetue a leitura de quatro notas reais de 10 alunos, 
# calcule e armazene em uma lista, a média de cada aluno, imprima o número 
# de alunos com média maior ou igual a 7.0.

avgs = []
higherThanSeven = 0

for i in range(10):
  total = 0

  for j in range(4):
    grade = float(input(f'Digite a {str((j+1))}° nota do {str((i+1))}° aluno: '))
    
    total += grade

  avg = total / 4

  avgs.append(avg)

  if avg >= 7:
    higherThanSeven += 1

print(f'A média dos 10 alunos são {avgs}, sendo {higherThanSeven} acima da média 7')