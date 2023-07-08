# Desafio com if, elif, else

'''
Criar um programa que dependendo da temperatura (em celsius)
do steak ele retorna o ponto de cozimento em portugues. O
usuário deverá fornecer a temperatura.

Temperaturas - Cozimento

120°F ou 48°C - Rare (Selada)
130°F ou 54°C - Medium rare (Ao ponto para o mal)
140°F ou 60°C - Medium (Ao ponto)
150°F ou 65°C - Medium Weel (Ao ponto para o bem)
160°F ou 71°C - Well done (Bem passada)
'''

temperatura = int(input("Qual é a temperatura da cane? "))

if temperatura < 48:
    print("Cozinha por mais alguns minutos.")
elif temperatura in range(48, 53):
    print("Rare (Selada)")
elif temperatura in range(54, 59):
    print("Medium rare (Ao ponto para o mal)")
elif temperatura in range(60, 64):
    print("Medium (Ao ponto)")
elif temperatura in range(65, 70):
    print("Medium Weel (Ao ponto para o bem)")
elif temperatura in range(71, 90):
    print("Well done (Bem passada)")
elif temperatura >= 91:
    print("A carne está queimada")
