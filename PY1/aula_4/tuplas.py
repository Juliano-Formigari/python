dia_semana = ('Domingo', 'Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado')
print(type(dia_semana))
print(dia_semana)
print(dia_semana[0])

print('\n\n')
for x in range(0, len(dia_semana)):
    print(dia_semana[x])
for x in range(0, len(dia_semana)):
    print(dia_semana[x].replace('-feira', ' Feira'))

print('\n\n')
pessoas = ('João', 'Maria', 'João', 'Pedro', 'Ana')
print(pessoas.count('João'))