# 4. Faça um Programa que leia três números e mostre o maior deles.

def maior(a, b):
    return a if a < b else b

a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
c = int(input("Terceiro número: "))

print("Maior:", maior(maior(a, b), c))

