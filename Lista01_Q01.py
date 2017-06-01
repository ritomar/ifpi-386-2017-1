try:
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))
    c = a + b
    print('A soma de %d com %d é:' % (a, b), c)
except:
    print('Você digitou algo errado.')
