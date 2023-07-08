# Desafio con Funções

'''
Criar um programa que calcula a quantidade de tinta necessária
para pintar uma parede. O usuário deverá fornecer as seguintes
informações: Rendimento, altura e largura.
O programa deve mostrar na tela a mensagem 'Voçê necessita
de x latas de tinta'
'''


def tinta():
    rendimento = float(input("Qual o rendimento da lata? "))
    altura = float(input("Qual é a altura da parede? "))
    largura = float(input("Qual é a largura da parede? "))

    total = (altura * largura) / rendimento

    return print(f"Você precisa de {total} latas de tinta")


tinta()
