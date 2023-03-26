# Operadores in e not in (estae entre e não estar entre)
# Strings são iteráveis ( navegar item por item)
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1
# nome = 'Otávio'
# print(nome[2])
# print(nome[-4])
# print('á' in nome)
# print('zero' in nome)
# print(10 * '-')
# print('vio' not in nome)
# print('zero' in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite oque deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')