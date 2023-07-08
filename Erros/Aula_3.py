# Erros
# Excelente para testes
# Não realiza o 'Stop' no programa
# Mensagens customizadas quando encontra um erro

try:
    valor = int(input("Digite o valor do seu produto: "))
    print(valor)
except ValueError:
    print("Favor digitar um valor em numeros")
# Executa mesmo se o usuario estiver errado
finally:
    print("Codigo ok")

# Não executa se o usuario digitar errado
# else:
#    print("Usuario digitou um valor correto")
#   resultado = valor * 2
#    print(resultado)

print("Mais codigo abaixo")
