# Unpacking Lists
# Armazenar mais de uma informação em variáveis
# Manter a sequencia dos dados em uma variável

produtos = ['arroz', 'feijão', 'laranja', 'banana', 5, 6, 7, 8]
#              0         1          2         3     4  5  6  7

item1, item2, item3, item4, *outros = produtos

print(item1)
print(item2)
print(item3)
print(item4)
print(outros)
