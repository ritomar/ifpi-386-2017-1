# 3. Verifique se um inteiro positivo n é primo.

n = int(input("Digite um número: "))

primo = True

i = 2

while i < (n // 2):
    if n % i == 0:
        primo = False
        break
    i += 1
    
if primo:
    print("%d é primo." % n)
else:
    print("%d não é primo." % n)
