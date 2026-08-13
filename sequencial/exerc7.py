#Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

try:
 lado = int(input("Digite o comprimento lado do quadrado: "))

 area = lado * lado
 print(f"A área do quadrado é de: {area}")

 dobro = area * 2
 print(f"O dobro da área é de: {dobro}")

except ValueError:
 print("DIgite um valor válido!!!")