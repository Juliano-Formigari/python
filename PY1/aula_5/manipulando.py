try:
    arq = open('arquivo.txt', 'r')
    arq.close()
except FileNotFoundError:
    arq = open('arquivo.txt', 'w')
    arq.close()
except:
    print('Ocorreu algum erro ao tentar abrir o arquivo')

try:
    arq = open('arquivo.txt', 'w')
    arq.write('Hello world')
    arq.close()
except: 
    print('Ocorreu algum erro ao tentar abrir o arquivo')

try:
    arq = open('arquivo.txt', 'w')
    arq.write('Welcome')
    arq.close()
except:
    print('Erro ao tentar o arquivo')


try:
    arq = open('arquivo.txt', 'r')
    conteudo = arq.read()
    print(conteudo)
    arq.close()
except:
    print('Erro ao tentar o arquivo')
