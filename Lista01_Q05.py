# 5) Solicite o preço de uma mercadoria e o percentual de desconto.
#    Exiba o valor do desconto e o preço a pagar.

val_merc = float(input("Valor da mercadoria: "))
per_desconto = float(input("% do desconto: "))
val_desconto = val_merc * (per_desconto / 100)
novo_valor = val_merc - val_desconto
print("Valor do Desconto: %.2f\nPreço a pagar: %.2f" % (val_desconto, novo_valor))

