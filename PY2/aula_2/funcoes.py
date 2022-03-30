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
    print('1 - Conta Corrente | 2 - Conta Poupança | 3 - Conta Salário')
    tipoConta = int(input('Informe a opção desejada:'))
    while (not tipoConta in [1,2,3]):
        print('Opção inválida')
        AguardaLimpa()
        print('1 - Conta Corrente | 2 - Conta Poupança | 3 - Conta Salário')
        tipoConta = int(input('Informe a opção desejada:'))
    return tipoConta