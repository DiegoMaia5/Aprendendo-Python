# List Comprehension
# Mais simples de se escrever
# Utilizado quando você precisa criar uma nova lista a partir de uma existente
# [expressão for iten in itens]

fruta1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']

# fruta2 = []

# for iten in fruta1:
#   if 'n' in iten:
#       fruta2.append(iten)

fruta2 = [iten for iten in fruta1 if 'b' in iten]

print(fruta2)
