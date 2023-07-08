# Functions (Funções)
# DRY - Don't repeat yourself.
# Vários Argumentos (xargs) identificando o Parametro.

# Criar uma função que armazena números e strings (dados)

# Colocando os dois asterisco você pode passar quantos Argumentos e quantos Argumentos quiser

def agencia(**carro):
    return carro


print(agencia(marca="Gol", cor="Branca", motor=1.0, placa=1234))
print(agencia(marca="Gol", cor="Vermelho", motor=1.0))
print(agencia(marca="Gol", cor="Azul", placa=1234))
