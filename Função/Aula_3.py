# Functions (Funções)
    # DRY -- Don't repeat yourself
    # Paramentro --> Argumento
    # Default = Aquele que você define o valor no parametro
    # Non-Default = Aquele que você não define o valor no parametro

# O Parametro Non-Default sempre vem primeiro

def boas_vindas(quantidade, nome="linda"):
    print(f"Olá {nome}.")
    print(f"Temos {str(quantidade)} laptops em estoque")

boas_vindas(5)