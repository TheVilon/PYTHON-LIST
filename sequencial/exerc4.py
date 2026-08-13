#Faça um programa que peça as 4 notas bimestrais e mostre a média.

nota1 = float(input(f"Digite a nota da primeira avaliação"))
nota2 = float(input(f"Digite a nota da segunda avaliação"))
nota3 = float(input(f"Digite a nota da terceira avaliação"))
nota4 = float(input(f"Digite a nota da quarta avaliação"))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"A média da nota do aluno é de: {media}")