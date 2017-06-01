# 2) Escreva um programa que leia um valor em metros
#    e o exiba convertido em milímetros

try:
    a = float(input('Digite um valor em metros: '))
    print('Valor em centímetros: %d' % (a * 1000))
except:
    print('Você digitou algo errado.')

