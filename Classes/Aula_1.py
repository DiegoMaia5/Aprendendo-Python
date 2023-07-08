# Python Object-Oriented Programming

# Classes
# Utilizadas para criar Objetos (instances)
# Objetos são partes dentro de uma Class (instances)
# Classes são utilizadas para agrupar dados e funções, podendo reutilizar
# ====
# Class: Frutas
# Objects: Abacate, Banana...


class Funcionario:
    nome = 'Diego'
    sobrenome = 'Maia'
    data_nascimento = '20/06/1995'


usuario1 = Funcionario

print(usuario1.nome)
print(usuario1.sobrenome)
print(usuario1.data_nascimento)
