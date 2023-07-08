# Python Object-Oriented Programming

# Classes
# Utilizadas para criar Objetos (instances)
# Objetos são partes dentro de uma Class (instances)
# Classes são utilizadas para agrupar dados e funções, podendo reutilizar
# ====
# Class: Frutas
# Objects: Abacate, Banana...

# Criar a classe
class Funcionario:
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento


# Criar o objeto
usuario1 = Funcionario('Elena', 'Cabral', '12/01/2009')
usuario2 = Funcionario('Carol', 'Silva', '15/10/2005')
usuario3 = Funcionario('Diego', 'Maia', '28/05/1995')

# Print

print(usuario1.nome)
print(usuario2.sobrenome)
print(usuario3.nome)
