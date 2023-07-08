# ===While Loops ===

# Excelente para loops dependentes de uma condição

# Criar uma promoção para um produto no valor de R$100.

valor = 100
dia = 1

while valor > 20:
    dia += 1
    print(f'No dia {dia} o produto estará R${valor}')
    valor -= 5
