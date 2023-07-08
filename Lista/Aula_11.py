# Set (Listas)
# Similar a listas
# Evitar itens duplicados
# Não utiliza index

s1 = {1, 2, 3, 4, 5, 6, 7}
# Forma mais simples de se utilizar o set

s1.update([6, 7, 8, 9, 10, 11])
# Para adicionar mais de um deve se utilizar o update

s1.remove(1)
s1.discard(90)

print(s1)
