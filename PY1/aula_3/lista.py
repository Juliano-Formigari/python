lista = [5, 3, 5.5, 'Juliano', True]
lista2 = ['Proway', lista]
print(lista2)
print(len(lista2))
print(type(lista2))
print(lista2[0])
print(type(lista2[0]))
print(lista2[1])
print(type(lista2[1]))

if type(lista2[0]) is str:
    print(lista2[0] + ' é uma String')