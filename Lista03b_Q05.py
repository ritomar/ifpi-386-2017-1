# 5. Faça um programa que peça um inteiro positivo e o mostre invertido.
# Ex.: 1234 gera 4321

n = int(input("Digite um número inteiro: "))

inv = 0

while n > 0:
    dig = n % 10
    n = n // 10
    inv = (inv * 10) + dig

print("Número invertido:", inv)
