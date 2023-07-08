# Functions (Função)
    # DRY - Don't repeat yourself.
    # Realizam uma tarefa
    # Calcula e retorna um valor


def cliente(nome):
    print(f"Olá {nome}")


def cliente2(nome):
    return f'Olá {nome}'


x = cliente('Maria')
y = cliente2('Jose')

print(x)
print(y)