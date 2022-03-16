loginPadrao = 'aluno'
senhaPadrao = 'proway'

aluno = input('Digite seu login: ')
senha = input('Digite sua senha: ')
while(aluno != loginPadrao or senha != senhaPadrao):
    print('Login e senha incorreta, digite novamente!!')
    aluno = input('Digite seu login: ')
    senha = input('Digite sua senha: ')

opcao = 1
saldo = 0

while(opcao > 0):
    print('BANCO PROWAY'.center(40, '-'))
    print('|1 - Sacar'.ljust(20, ' ') + '|2 - Depositar'.ljust(20, ' ') + '|')
    print('|3 - Transferir'.ljust(20, ' ') + '|4 - Ver Saldo'.ljust(20, ' ') + '|')
    print('|' + '5 - Sair'.center(39) + '|')
    print(''.center(40, '-'))
    opcao = int(input('Operação desejada: '))
    match opcao:
        case 1:
            valor = int(input('Valor para saque: '))
            if(valor > saldo):
                print('Saldo insuficiente!')
            else:
                saldo -= valor
                print('Saque efetuado com sucesso')
        case 2:
            valor = int(input('Valor para depósito: '))
            saldo += valor
        case 3:
            valor = int(input('Valor para transferência: '))
            if(valor > saldo):
                print('Saldo insuficiente!')
            else:
                conta = input('Conta para transferência\n\n')
                if(len(conta) == 5):
                    saldo -= valor
                    print('Transferência efetuada com sucesso!')
                else:
                    print('Conta inválida!')
        case 4:
            print('Saldo atual: ' + str(saldo))
        case 5:
            print('Sair')
            break
        case default:
            print('Opção inválida')
