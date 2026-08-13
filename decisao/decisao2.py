'''
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média 
alcançada por aluno e apresentar:

A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''
# Validação da Nota 1
while True:
    try:
        nota1 = float(input("Digite a nota da primeira avaliação: "))
        if 0 <= nota1 <= 10:
            break  # Nota válida! Sai do loop.
        print("Digite o valor de nota válida (entre 0 e 10).")
    except ValueError:
        print("Erro! Use apenas números e use PONTO em vez de vírgula (Ex: 7.5).")

# Validação da Nota 2
while True:
    try:
        nota2 = float(input("Digite a nota da segunda avaliação: "))
        if 0 <= nota2 <= 10:
            break  # Nota válida! Sai do loop.
        print("Digite o valor de nota válida (entre 0 e 10).")
    except ValueError:
        print("Erro! Use apenas números e use PONTO em vez de vírgula (Ex: 7.5).")

# Cálculo da Média
media = (nota1 + nota2) / 2
print(f"\nMédia: {media:.1f}")

# Verificação do Resultado
if media == 10:
    print("Aprovado com distinção")
elif 7.0 <= media < 10:
    print("Aprovado")
else:
    print("Reprovado")
