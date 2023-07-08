from sys import getsizeof

# Generator Expressions
# Uma forma mais rápida para Listas, Dicionários e etc
# Menos memória alocada
# Valores em bytes

# Formato de lista alocando mais memória
numeros = [x * 10 for x in range(10000)]

print(type(numeros))
print(getsizeof(numeros))

print("===========")

# Generator Expressions alocando menos memória
numeros = (x * 10 for x in range(10000))
print(type(numeros))
print(getsizeof(numeros))
