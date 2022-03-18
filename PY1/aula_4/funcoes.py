import os
import time

def mensagem(pValor):
    print(pValor)

def mensagem2():
    print('Welcome!')

def somaValores(pValor1, pValor2):
    print('A soma dos valores é ' + str(pValor1 + pValor2))

os.system('cls')
time.sleep(3)
mensagem('Adoro programar em Python')
somaValores(10, 5)


