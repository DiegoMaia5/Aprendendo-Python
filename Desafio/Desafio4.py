import os
# Calculo IMC - Índice de Massa Corporal

'''
Qual é a sua altura em cm:
Qual é o seu peso em Kg:
'''

# Menor que 18,5 Magreza
# Entre 18,5 e 24,9 Normal
# Entre 25,0 e 29,9 Sobrepeso
# Entre 30,0 e 39,9 Obesidade
# Maior que 40,0 Obesidade Grave

altura = float(input("Qual é a sua altura em cm? ")) 
peso = float(input("Qual é o seu peso em kg? "))

imc = peso / (altura/100)**2

print(f"Seu Índice de Massa Corporal é {imc:.2f}")

if imc < 18.5:
    print("Magreza")
elif imc < 24.9:
    print("Normal")
elif imc < 29.9:
    print("Sobrepeso")
elif imc < 39.9:
    print("Obesidade")
else:
    print("Obesidade Grave")
    