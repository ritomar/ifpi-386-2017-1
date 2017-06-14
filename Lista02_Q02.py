# 2. Determine se um ano é bissexto. Verifique no Google como fazer isso...

def e_bissexto(ano):
    return (ano % 400 == 0) or ((ano % 4 == 0) and (ano % 100 != 0))


print("Verificação de Ano Bissexto")
a = int(input("Digite um ano: "))
if e_bissexto(a):
    print("%d é um ano bissexto." % a)
else:
    print("%d NÃO é um ano bissexto." % a)
