"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input("Digite a hora atual (formato 24 horas): ")

try:
    hora = int(hora)
    if hora >= 0 and hora <= 11:
        print("Bom dia!")
    elif hora >= 12 and hora <= 17:
        print("Boa tarde!")
    elif hora >= 18 and hora <= 23:
        print("Boa noite!")
    else:
        print("Hora inválida. Insira um valor entre 0 e 23.")
except ValueError:
    print("Valor inválido. Insira um número inteiro entre 0 e 23.")
