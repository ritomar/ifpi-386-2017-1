# 4. Dado um número inteiro positivo, determine a sua decomposição em fatores
# primos calculando também a multiplicidade de cada fator# 4. Dado um número inteiro positivo, determine a sua decomposição em fatores
# primos calculando também a multiplicidade de cada fator.

def E_Primo(n):
    primo = n > 1
    i = 2
    while i < n // 2:
        if n % i == 0:
            primo = False
            break
        i += 1
    return primo

def Proximo_Primo(n):
    i = n + 1
    while True:
        if E_Primo(i):
            return i
        else:
            i += 1

def E_Divisivel(n, m):
    return n % m == 0

num = int(input("Digite um número para decompor: "))

n = num
primo = 1
msg = ""

while (n > 1):
    primo = Proximo_Primo(primo)
    multiplicidade = 0
    while E_Divisivel(n, primo):
        print("%6d | %3d" % (n, primo))
        multiplicidade += 1
        n = n // primo
    if multiplicidade > 0:
        if msg != "":
            msg += "x "
        if multiplicidade > 1:
            msg = msg + "%d^%d " % (primo, multiplicidade)
        else:
            msg = msg + "%d " % (primo)
        
print("%6d |\n\n%d = %s" % (n, num, msg))
    
