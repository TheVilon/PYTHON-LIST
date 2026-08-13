#Faça um programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input("Digite uma letra: "))

if letra.lower() in 'aeiou':
    print("Essa letra é uma vogal !")
else:
    print("Essa letra é um consoante !")