# 2. Indique como um troco deve ser dado utilizando-se um número mínimo de
# notas. Seu algoritmo deve ler o valor da conta a ser paga e o valor do
# pagamento efetuado desprezando os centavos. Suponha que as notas para troco
# sejam as de 50, 20, 10, 5, 2 e 1 reais, e que nenhuma delas esteja em
# falta no caixa.

valor_conta = int(input("Valor da conta: "))
valor_pago = int(input("Valor pago: "))

troco = valor_pago - valor_conta

n50 = troco // 50
troco = troco % 50

n20 = troco // 20
troco = troco % 20

n10 = troco // 10
troco = troco % 10

n5 = troco // 5
troco = troco % 5

n2 = troco // 2
troco = troco % 2

n1 = troco

print("R$  1.00 x %d" % n1)
print("R$  2.00 x %d" % n2)
print("R$  5.00 x %d" % n5)
print("R$ 10.00 x %d" % n10)
print("R$ 20.00 x %d" % n20)
print("R$ 50.00 x %d" % n50)
