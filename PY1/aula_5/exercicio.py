# Elabore um programa para manipular informações em uma lista.
# Os itens da lista deverão ser arquivos de informática
# A cada operação executada (leitura, inserção, exclusão e edição da lista deverá gravar um log)
# O arquivo será "log.txt"
# Implementar a função grava log e demais funções em arquivo separado.
# A função gravaLog deverá receber uma mensagem de parâmetro que será gravada.
# Tempo estimado: 20 minutos
import controller
import os
import time
op = 0
lista = []
while ( op != 5 ):
    time.sleep(3)
    os.system('cls')
    op = int(input('Operação desejada: \n' + 
                   '1- Cadastrar   | 2- Visualizar \n' + 
                   '3- Alterar     | 4- Excluir \n' + 
                   '            5- Sair\n'))
    match op:
        case 1:
            controller.gravaLog('Opção Cadastrar\n')
            valor = input('Informe o item que deseja cadastrar: ')
            controller.inserir(lista,valor)
        case 2:
            controller.gravaLog('Opção Listar\n')
            controller.exibir(lista)
        case 3:
            controller.gravaLog('Opção Alterar\n')
            valor = input('Qual item deseja alterar? ')
            controller.alterar(lista,valor)
        case 4:
            controller.gravaLog('Opção Excluir\n')
            valor = input('Item que deseja excluir: ')
            controller.excluir(lista,valor)
        case 5:
            controller.gravaLog('Saiu do sistema\n')
            print('Saindo...')
            break
        case outrocaso:
            controller.gravaLog('Opção inválida\n')
            print('Opção inválida')