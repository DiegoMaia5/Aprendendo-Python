# Listas
# Armazenar mais de uma informação em váriaveis
# Manter a sequencia dos dados em uma váriavel

cor_cliente = input("Digite uma cor desejada: ")
cores = ['amarelo', 'verde', 'azul', 'vermelho']

if cor_cliente.lower() in cores:
    print('Em estoque')
else:
    print('Não temos esta cor em estoque')
