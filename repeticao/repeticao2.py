"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações.
"""
while True:
    try:
        usuario = str(input("Insira um nome de usuário: "))
        senha = input("Digite uma senha: \n")
        if senha != usuario:
            print("Senha criada com sucesso !")
            break
        else:
            print("A senha não pode ser o seu nome do usuário apenas!!!")
    except ValueError:
        print("Digite uma senha válida")