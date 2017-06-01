# 9) Escreva um programa que pergunte a quantidade de km percorridos
#    por um carro alugado pelo usuário, assim como a quantidade de
#    dias pelos quais o carro foi alugado. Calcule o preço a pagar,
#    sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

quantidade_de_km = float(input("Quantidade de Km percorridos: "))
dias = int(input("Quantidade de dias: "))

preco = (dias * 60) + (quantidade_de_km * 0.15)

print("Total:", preco)
