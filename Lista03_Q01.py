# 1. Faça um programa que peça uma nota, entre zero e dez.
#    Mostre uma mensagem caso o valor seja inválido e continue pedindo
#    até que o usuário informe um valor válido.


n = float(input("Digite uma nota entre zero e dez: "))
while n < 0 or n > 10:
    print("Valor inválido.")
    n = float(input("Digite uma nota entre zero e dez: "))

print("Nota:", n)
