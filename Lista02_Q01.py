# 1. Faça um Programa que peça os três lados de um triângulo.
#    O programa deverá informar se os valores podem ser um triângulo.
#    Indique, caso os lados formem um triângulo, se o mesmo é:
#    equilátero, isósceles ou escaleno.

def e_triangulo(a, b, c):
    return (a < b + c) and (b < a + b) and (c < a + b)

def e_triangulo_equilatero(a, b, c):
    return e_triangulo(a, b, c) and ((a == b) and (b == c) and (c == a))

def e_triangulo_isosceles(a, b, c):
    return e_triangulo(a, b, c) and ((a == b) or (b == c) or (a == c))

def e_triangulo_escaleno(a, b, c):
    return e_triangulo(a, b, c) and ((a != b) and (b != c) and (c != a))

print("Verificação de Triângulos")
x = int(input("Primeiro lado: "))
y = int(input("Segundo lado: "))
z = int(input("Terceiro lado: "))

if (e_triangulo(x, y, z)):
    if (e_triangulo_equilatero(x, y, z)):
        print("Os lados %d, %d e %d formam um triângulo equilátero." % (x, y, z))
    elif (e_triangulo_isosceles(x, y, z)):
        print("Os lados %d, %d e %d formam um triângulo isósceles." % (x, y, z))
    elif (e_triangulo_escaleno(x, y, z)):
        print("Os lados %d, %d e %d formam um triângulo escaleno." % (x, y, z))
else:
    print("Os lados %d, %d e %d não formam um triângulo." % (x, y, z))

