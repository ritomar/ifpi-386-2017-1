# 4. A seqüência de Fibonacci é a seguinte:
#    1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
#    Sua regra de formação é simples: os dois primeiros elementos são 1;
#    a partir de então, cada elemento é a soma dos dois anteriores.
#    Faça um algoritmo que leia um número inteiro calcule o seu número
#    de Fibonacci. F1 = 1, F2 = 1, F3 = 2, etc.

def Fibonacci(n):
    t0 = 1
    t1 = 1
    if n == 1:
        return fib = str(t0)
    elif n == 2:
        return fib = str(t0) + " " + str(t1)
    elif n > 2:
        for i in range (3, n + 1):
            tn = t0 + t1
            fib = fib + " " + str(tn)
            t0, t1 = t1, tn
        return fib
    else:
        return "Quantidade inválida de termos."

k = int(input("Quantidade de Termos para Fibonacci: "))
print(Fibonacci(k))
