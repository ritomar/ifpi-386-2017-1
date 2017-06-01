# 10) Escreva um programa para calcular a redução do tempo de vida de
#     um fumante. Pergunte a quantidade de cigarros fumados por dia e
#     quantos anos ele já fumou. Considere que um fumante perde 10 minutos
#     de vida a cada cigarro, calcule quantos dias de vida um fumante
#     perderá. Exiba o total de dias.

cigarros_dia = int(input("Cigarros fumados por dia: "))
anos_fumando = int(input("Quantos anos fumando: "))

total_cigarros = cigarros_dia * (anos_fumando * 365)

dias_perdidos = ((total_cigarros * 10) / 60) / 24

print("Dias perdidos:", dias_perdidos)
