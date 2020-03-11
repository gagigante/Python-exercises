speed = int(input('Informe a velocidade do projeto'))
angle = int(input('Informe o ângulo entre o cano do canhão e o solo (GRAUS)'))

reach = (speed * speed / 10) * (2 * angle)

print(reach)