nome = 'Aleyson Garcia'
altura = 1.74
peso = 50
imc = peso / (altura * altura)  #IMC = Peso / altura x altura - eu poderia ter usado altura *2

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso:.2f} quilos e seu IMC é {imc:.2f}'

print(linha_1)
print(linha_2)