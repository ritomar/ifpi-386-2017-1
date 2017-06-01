# 3) Escreva um programa que leia a quantidade de dias, horas,
#    minutos e segundos do usuário. Calcule o total em segundos.

try:
    dias = int(input("Dias: "))
    horas = int(input("Horas: "))
    minutos = int(input("Minutos: "))
    segundos = int(input("Segundos: "))
    total_segundos = (dias * 24 * 60 * 60) + (horas * 60 * 60) + (minutos * 60) + segundos
    
    print("Total em segundos: %d" % total_segundos)
except:
    print("Você digitou algo errado.")

