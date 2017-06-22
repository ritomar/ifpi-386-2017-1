# 3. Supondo que a população de um país A seja da ordem de 80000
#    habitantes com uma taxa anual de crescimento de 3% e que a população
#    de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
#    Faça um programa que calcule e escreva o número de anos necessários
#    para que a população do país A ultrapasse ou iguale a população do
#    país B, mantidas as taxas de crescimento


popA = 80000
popB = 200000
txA = 0.030
txB = 0.015
anos =  0
while popA < popB:
    popA *= (1 + txA)
    popB *= (1 + txB)
    anos += 1

print("Pop A: %d; Pop B: %d; Anos: %d" % (popA, popB, anos))


