"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}') #ele preenche varias casas com espaço ou com oq quiser
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{1000.489827198271991:0=+10,.1f}')
print(f'{variavel!r}')