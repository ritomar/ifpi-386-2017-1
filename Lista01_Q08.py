# 8) Faça agora o contrário, de Fahrenheit para Celsius.
#    C = (F - 32) * (5/9)

temp_f = float(input("Temperatura em Fahrenheit: "))

temp_c = (temp_f - 32) * (5/9)

print("Temperatura em Celsius: %.2f" % (temp_c))
