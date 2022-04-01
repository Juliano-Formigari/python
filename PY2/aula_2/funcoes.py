from email.policy import default
import os
import time

def LimpaTela():
    os.system('cls')

def Aguarda():
    time.sleep(4)

def AguardaLimpa():
    Aguarda()
    LimpaTela()

def validaTipoConta():
    tipoConta = 0
    print('1 - Conta Corrente | 2 - Conta Poupança | 3 - Conta Salário | 4 - Todas')
    tipoConta = int(input('Informe a opção desejada:'))
    while (not tipoConta in [1,2,3,4]):
        print('Opção inválida')
        AguardaLimpa()
        print('1 - Conta Corrente | 2 - Conta Poupança | 3 - Conta Salário | 4 - Todas')
        tipoConta = int(input('Informe a opção desejada:'))
    return tipoConta

def menuOperacoes(pTipoConta):
    opcao = 0
    AguardaLimpa()
    print('Operação desejada: \n')
    match pTipoConta:
        case 1, 2:
            while (not (opcao in [1, 2, 3, 4, 5])):
                print('Opção inválida!')
            return int(input('1 - Sacar | 2 - Depositar | 3 - Transferir | 4 - Ver Saldo | 5 - Voltar \n'))
        case 3:
            while (not (opcao in [1, 2, 3])):
                print('Opção inválida!')
            return int(input('1 - Sacar | 2 - Ver Saldo | 3 - Voltar \n'))
        case default:
            pass
