# 5. Dados dois números inteiros positivos, determinar o máximo divisor
#    comum entre eles usando o algoritmo de Euclides.


def MDC(a, b):
    while (b != 0):
        q = a / b
        r = a % b
        a = b
        b = r
    return a

a, b = 348, 156
print("MDC de %d e %d é: %d" % (a, b, MDC(a, b)))
