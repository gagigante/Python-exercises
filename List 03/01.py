# Uma empresa decidiu fazer um levantamento em relação aos candidatos que se 
# apresentarem para preenchimento de vagas em seu quadro de funcionários. 
# Supondo que você seja o programador dessa empresa, faça um programa que leia, 
# para cada candidato, a idade, o sexo (M ou F), e a experiência no serviço (S ou N). 
# Para encerrar a entrada de dados, digite a idade igual a zero. 
# O programa também deve calcular e mostrar:

# O número de candidatos do sexo feminino.
# O número de candidatos do sexo masculino.
# A idade média dos homens que já tem experiência no serviço.
# A porcentagem dos homens com mais de 45 anos entre o total dos homens.
# O número de mulheres com idade inferior a 21 anos e com experiência no serviço.
# A menor idade entre as mulheres que já tem experiência no serviço.

femaleQtt = 0
maleQtt = 0
averageAgeOfExperiencedMales = 0 
totalExperiencedMalesAge = 0
qttExperiencedMales = 0
qttMalesOrderThan45 = 0
qttExperiencedFamalesYoungerThan21 = 0
youngerExperiencedFamale = 0

while True:
  age = int(input('Informe sua idade '))

  if age == 0:
    break

  gender = str(input('Informe seu gênero (M ou F) '))
  experience = str(input('Informe a experiência no serviço (S ou N) '))

  if gender == 'M':
    maleQtt += 1

    if experience == 'S':
      totalExperiencedMalesAge += age
      qttExperiencedMales += 1

    if age > 45:
      qttMalesOrderThan45 += 1
  else:
    femaleQtt += 1

    if age < 21:
      if experience == 'S':
        qttExperiencedFamalesYoungerThan21 += 1

    if youngerExperiencedFamale == 0 or age < youngerExperiencedFamale:
      youngerExperiencedFamale = age

percentOfMalesOrderThan45 = (maleQtt / qttMalesOrderThan45) * 100

print(f'A quantidade de mulheres é {femaleQtt}')
print(f'A quantidade de homens é {maleQtt}')
print(f'A idade média de homens com experiência é {totalExperiencedMalesAge / qttExperiencedMales}')
print(f'A porcentagem de homens mais velhos que 45 anos é {percentOfMalesOrderThan45}')
print(f'A quantidade de mulheres com experiência e menores que 21 anos é {qttExperiencedFamalesYoungerThan21}')
print(f'A idade da mulher com experiência mais jovem é {youngerExperiencedFamale}')




