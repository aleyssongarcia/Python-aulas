'''
Introdução ao try/except
try -> tentar executar o codigo
execept -> ocorreu algum erro ao tentar executar
'''
numero_str = input(
    'Vou dobrar o número que vc digitar: ')

try:

    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
     print('isso não é um número')

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('isso não é um número')