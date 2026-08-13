"""
Faça um programa que pergunte quanto você ganha por hora 
e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
"""
valor_hora = float(input("Digite o valor da sua horas: "))
hora_trabalhada = int(input("Qauntas horas você trabalhou no mês: "))

salario = valor_hora * hora_trabalhada
print(f"O seu salário do Mês é de: R${salario}")