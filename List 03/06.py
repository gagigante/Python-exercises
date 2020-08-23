# Faça um programa que apresente a soma dos cem primeiros números naturais (1+2+3+4+5+...+98+99+100)

total = 0

for i in range(1, 101):
  total += i

print(total)