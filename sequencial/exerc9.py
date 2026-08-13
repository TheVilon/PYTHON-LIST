"""
Faça um programa que peça 
a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
"""
try:
    F = float(input("Digite a temperatura atual em Fahrenheit: "))

    celsius = 5 * ((F-32) / 9)

    print(f"A temperatura atual em Celsius é: {celsius:.1f}°")
except ValueError:
    print("Digite um valor válido!!!")