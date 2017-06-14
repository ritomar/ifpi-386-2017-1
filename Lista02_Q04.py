# 4. Faça um Programa que leia três números e mostre o maior deles.

a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
c = int(input("Terceiro número: "))

if a >= b and a >= c:
    maior = a
elif b >= a and b >= c:
    maior = b
elif c >= a and c >= b:
    maior = c

print("Maior:", maior)
