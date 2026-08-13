#Faça um programa que peça o raio de um círculo, calcule e mostre sua área:

import math

try:
 raio = float(input("Digite o raio do círculo: "))
 print(raio)

 r2 = raio ** 2
 print(r2)

 area = r2 * math.pi
 print(f"A área do círculo é de: {area:.2f}")

except ValueError:
 print("Digite um valor Válido!!!")