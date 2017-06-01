# 6) Calcule o tempo de uma viagem de carro.
#    Pergunte a distância a percorrer e a velocidade média
#    esperada para a viagem.

distancia = float(input("Distância(Km): "))
vm = float(input("Velocidade média(Km/h): "))

minutos = (distancia / vm) * 60

horas = minutos // 60
minutos = minutos % 60

print("Tempo da viagem %d horas e %d minutos." % (horas, minutos))
