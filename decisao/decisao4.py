#Faça um programa que leia três números e mostre-os em ordem decrescente:

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))
numero3 = int(input("Digite mais um número: "))

descressente = sorted([numero1, numero2, numero3], reverse =True)
print("Os números em ordem decrescente são:", descressente)

# Faça um programa que leia três números e mostre-os em ordem crescente:
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite mais um número: "))

crescente = sorted([n1, n2, n3], reverse=False)
print("Os números em ordem crescente são:", crescente)