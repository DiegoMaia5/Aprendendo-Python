# Functions (Funções)
    # DRY - Don't repeat yourself.
    # Vários Argumentos (xargs)

# Criar uma função que soma vários números.

def soma(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado

x = soma(1,4,5,6)

print(x)