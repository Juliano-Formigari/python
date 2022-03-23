from genericpath import exists


sucesso_Inserir = ' inserido com sucesso!'
sucesso_Excluir = ' excluído com sucesso!'
lista_vazia = 'Lista vazia!'
inexistente = ' não está cadastrado!'

def inserir(obj,valor):
    obj.append(valor)
    print(valor + sucesso_Inserir)

def excluir(obj,valor):
    if len(obj) == 0:
        print(lista_vazia)
    if valor in obj:
        obj.remove(valor)
        print(valor + sucesso_Excluir)
    print(valor + inexistente)

def exibir(obj):
    if len(obj) == 0:
        print(lista_vazia)
    print(obj)

def alterar(obj,valor):
    if len(obj) == 0:
        print(lista_vazia)
    if not ( valor in obj ):
        print(valor + inexistente)
        return
    novo = input('Informe o novo valor para ' + valor + ': ')
    for x in range(0,len(obj)):
        if obj[x] == valor:
            obj[x] = novo
            print(valor + ' alterado para ' + novo + '!')

def gravaLog(mensagem):
    if exists('log.txt'):
        arq = open('log.txt','a')
    else:
        arq = open('log.txt','w')
    arq.write(mensagem)
    arq.close()
