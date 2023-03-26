"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""


# num = input("Digite um número inteiro: ")

# try:
#     num = int(num)
#     if num % 2 == 0:
#         print(f"O número {num} é par.")
#     else:
#         print(f"O número {num} é ímpar.")
# except ValueError:
#     print("O valor digitado não é um número inteiro.")

entrada = input('Digite um número: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
else:
    print('Você não digitou um número.')