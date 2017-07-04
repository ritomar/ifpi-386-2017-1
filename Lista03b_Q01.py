# 1. Dizemos que um número natural é triangular se ele é produto de três números
# naturais consecutivos. Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um
# inteiro não-negativo n, verificar se n é triangular.

n = int(input("Digite um número: "))

triangular = False
i = 1

while True:
    teste = (i * (i + 1) * (i + 2))
    if teste == n:
        triangular = True
        break
    elif teste > n:
        triangular = False
        break
    else:
        i += 1
if triangular:
    print("%d x %d x %d = %d -> é triangular." % (i, i+1, i+2, n))
else:
    print("%d não é triangular." % n)
