# Dicionários
# Utiliza index no formato de Keys e Values
# Aceita string, integer, float, boolean...

aluno = {'nome': 'Diego', 'idade': 16, 'nota_final': 'A', 'aprovação': True}

# aluno.update({'endereço': 'Rua A'})

print(aluno.get('endereço', 'Não existe'))
