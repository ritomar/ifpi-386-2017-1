# 7) Converta uma temperatura digitada em Celsius para Fahrenheit.
#    F = 9 * C / 5 + 32

temp_c = float(input("Temperatura em Celsius: "))

temp_f = (temp_c * (9/5)) + 32

print("Temperatura em Fahrenheit: %.2f" % (temp_f))
