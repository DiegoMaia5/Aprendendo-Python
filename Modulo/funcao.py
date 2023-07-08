def somar():
    print("Essa funcao ira somar")


def multi():
    print("Essa funcao ira multiplicar")


def find_index(to_find, item):
    for i, valor in enumerate(to_find):
        if valor == item:
            return i
    return -1
