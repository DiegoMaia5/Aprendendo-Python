from datetime import datetime
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
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome

    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento


# Criar o objeto
usuario1 = Funcionario('Elena', 'Cabral', 2014)
usuario2 = Funcionario('Carol', 'Silva', 2005)
usuario3 = Funcionario('Diego', 'Maia', 1995)

# Print
print(Funcionario.idade_funcionario(usuario1))
