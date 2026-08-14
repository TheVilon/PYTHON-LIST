"""
Faça um programa que leia e valide as seguintes informações:

Nome: maior que 3 caracteres;
Idade: entre 0 e 120;
Salário: maior que zero;
Estado Civil: 's', 'c', 'v', 'd';

"""
while True:
        nome = input("Digite seu nome: ")
        if len(nome) > 3:
            print(f"Prazer, {nome}")
            break
        print("O seu nome deve conter mais do que 3 caracteres !")