"""
Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
"""


while True:
    try:
        numero = float(input("Digite uma nota entre 0 á 10: "))
        if 0 <= numero <= 10:
            print("Nota aceita!")
            break
        else:
            print(f"Digite um valor de nota válidas, você escreveu {numero}")
    except ValueError:
        print("Digite um valor válido!")
