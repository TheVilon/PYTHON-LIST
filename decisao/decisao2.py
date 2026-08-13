"""
Faça um programa que pergunte o preço de três produtos e informe qual produto você 
deve comprar, sabendo que a decisão é sempre pelo mais barato:
"""
produto1= float(input("Digite o preço do primeiro produto: "))
produto2= float(input("Digite o preço do segundo produto: "))
produto3= float(input("Digite o preço do terceiro produto: "))

if produto1 < produto2 and produto1 < produto3:
    print("Você deve comprar o primeiro produto, que custa R$", produto1)
elif produto2 < produto1 and produto2 < produto3:
    print("Você deve comprar o segundo produto, que custa R$", produto2)
else:
    print("Você deve comprar o terceiro produto, que custa R$", produto3)