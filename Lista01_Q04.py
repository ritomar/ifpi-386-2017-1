# 4) Faça um programa que calcule o aumento de um salário.
#    Ele deve solicitar o valor do salário e a porcentagem do aumento.
#    Exiba o valor do aumento e do novo salário.

try:
    val_sal = float(input("Valor do salário: "))
    per_aumento = float(input("% do aumento: "))
    val_aumento = val_sal * (per_aumento / 100)
    novo_sal = val_sal + val_aumento
    
    print("Valor do Aumento: %.2f\nNovo Salário: %.2f" % (val_aumento, novo_sal))
except:
    print("Você digitou algo errado.")

