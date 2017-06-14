# 4. Faça um Programa que leia três números e mostre o maior deles.

a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
c = int(input("Terceiro número: "))

if a >= b:
    maior = a
else:
    maior = b
    
if maior < c:
    maior = c
    
print("Maior:", maior)
