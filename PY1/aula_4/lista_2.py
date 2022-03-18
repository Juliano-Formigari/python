lista = ['dois']
print(lista)
lista.append('três')
print(lista)
lista.insert(0,'um')
print(lista)
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)

lista.pop(1)
print(lista)
lista.remove('dois')
lista[0] = 'segundo'
print(lista)
lista.insert(0,'um')

for x in range(0, len(lista)):
    print(str(x + 1 ) + 'º item -> ' + lista[x])
