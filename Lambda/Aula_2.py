# Lambda Function
# è uma função (pequena) sem nome
# Pode ter vários argumentos mas somente 1 expressão
# Muito utilizada dentro de outras funções
# Código mais 'clean'

# def somar(x):
#     return x + 10

# print(somar(2))

def somar(x):
    def func2(x): return x + 10
    return func2(x) * 4


print(somar(2))
