from classeContaCorrente import ContaCorrente
from classeContaPoupanca import ContaPoupanca
from classeContaSalario import ContaSalario
import funcoes as f
import constantes as cons


contasC = {} #Conta Corrente
contasP = {} #Conta Poupança
contasS = {} #Conta Salário

opcao = 0
tipoConta = 0

f.LimpaTela()

while opcao != 5:
    print('Banco PROWAY')
    print('1 - Criar Conta | 2 - Listar Contas | 3 - Excluir Contas | 4 - Operações | 5 - Sair')
    opcao = int(input('Informe a opção desejada: \n'))
    f.LimpaTela()

    match opcao:
        case 1:
            tipoConta = f.validaTipoConta()
            f.LimpaTela()
            numero = input(cons.MSG_CONTA_CADASTRAR)
            if (not f.validaTamanhoConta(numero)):
                f.AguardaLimpa()
            else:
                match tipoConta:
                    case 1:
                        if not(f.existeConta(numero, contasC, True)):
                            c = ContaCorrente(numero)
                            contasC[c.numeroConta] = 0
                            print(cons.MSG_SUCESSO_CADATRAR)
                            del(c)
                    case 2:
                        if not(f.existeConta(numero, contasP, True)):
                            c = ContaPoupanca(numero)
                            contasP[c.numeroConta] = 0
                            print(cons.MSG_SUCESSO_CADATRAR)
                            del(c)
                    case default:
                        if not(f.existeConta(numero, contasS, True)):
                            c = ContaSalario(numero)
                            contasS[c.numeroConta] = 0
                            print(cons.MSG_SUCESSO_CADATRAR)                            
                            del(c)
            f.AguardaLimpa()
        case 2:
            tipoConta = f.validaTipoConta(True)
            f.LimpaTela()
            match tipoConta:
                case 1:
                    if (f.existeContaCadastrada(contasC, tipoConta)):
                        print(contasC)
                case 2:
                    if (f.existeContaCadastrada(contasP, tipoConta)):
                        print(contasP) 
                case 3:
                    if (f.existeContaCadastrada(contasS, tipoConta)):
                        print(contasS)
                case default:
                    print('Contas Correntes: ')
                    print(contasC)
                    print('Contas poupanças: ')
                    print(contasP)
                    print('Contas salário: ')
                    print(contasS)
            f.AguardaLimpa()
        case 3:
            tipoConta = f.validaTipoConta()
            f.LimpaTela()
            match tipoConta:
                case 1:
                    if f.existeContaCadastrada(contasC, tipoConta):
                        numero = input(cons.MSG_CONTA_EXCLUIR + '\n')
                        if f.validaTamanhoConta(numero):
                            if f.existeConta(numero, contasC):
                                c = ContaCorrente(numero)
                                contasC.pop(c.numeroConta)
                                print(cons.MSG_SUCESSO_EXCLUIR)
                                del(c)
                case 2:
                    if f.existeContaCadastrada(contasP, tipoConta):
                        numero = input(cons.MSG_CONTA_EXCLUIR + '\n')
                        if f.validaTamanhoConta(numero):
                            if f.existeConta(numero, contasP):
                                c = ContaPoupanca(numero)
                                contasP.pop(c.numeroConta)
                                print(cons.MSG_SUCESSO_EXCLUIR)
                                del(c)
                case default:
                    if f.existeContaCadastrada(contasS, tipoConta):
                        numero = input(cons.MSG_CONTA_EXCLUIR + '\n')
                        if f.validaTamanhoConta(numero):
                            if f.existeConta(numero, contasS):
                                c = ContaSalario(numero)
                                contasS.pop(c.numeroConta)
                                print(cons.MSG_SUCESSO_EXCLUIR)
                                del(c)
            f.AguardaLimpa()
        case 4:
            tipoConta = f.validaTipoConta()
            match tipoConta:
                case 1:
                    opcao = f.menuOperacoes(tipoConta)
                    match opcao:
                        case 1:
                            numero = input(cons.MSG_NUMERO_CONTA)
                            if f.validaTamanhoConta(numero):
                                if f.existeConta(numero, contasC):
                                    valor = int(input(cons.MSG_VALOR_SAQUE))
                                    if f.existeSaldo(numero, contasC, tipoConta, valor):
                                        contasC[numero] -= valor
                                        print(cons.MSG_SUCESSO_SAQUE)
                        case 2:
                            numero = input(cons.MSG_NUMERO_CONTA)
                            if f.existeConta(numero, contasC):
                                valor = int(input(cons.MSG_VALOR_DEPOSITO))
                                contasC[numero] += valor
                                print(cons.MSG_SUCESSO_DEPOSITO)
                        case 3:
                            numero = input(cons.MSG_NUMERO_CONTA)
                            if f.validaTamanhoConta(numero):
                                if f.existeConta(numero, contasC):
                                    numeroContaDestino = input(cons.MSG_NUMERO_CONTA_DESTINO)
                                    tipoDestino = f.validaTipoConta()
                                    match tipoDestino:
                                        case 1:
                                            if f.existeConta(numeroContaDestino, contasC):
                                                valor = int(input(cons.MSG_VALOR_TRANSFERENCIA))
                                                if f.existeSaldo(numero, contasC, tipoConta, valor):
                                                    contasC[numero] -= (valor + (valor * 0.05))
                                                    contasC[numeroContaDestino] += valor
                                        case 2:
                                            if f.existeConta(numeroContaDestino, contasP):
                                                valor = int(input(cons.MSG_VALOR_TRANSFERENCIA))
                                                if f.existeSaldo(numero, contasC, tipoConta, valor):
                                                    contasC[numero] -= valor
                                                    contasP[numeroContaDestino] += valor
                                        case default:
                                            if f.existeConta(numeroContaDestino, contasS):
                                                valor = int(input(cons.MSG_VALOR_TRANSFERENCIA))
                                                if f.existeSaldo(numero, contasC, tipoConta, valor):
                                                    contasC[numero] -= valor
                                                    contasS[numeroContaDestino] += valor
                                print(cons.MSG_SUCESSO_TRANSFERENCIA)
                        case 4:
                            numero = input(cons.MSG_NUMERO_CONTA)
                            if f.validaTamanhoConta(numero):
                                if f.existeConta(numero, contasC):
                                    print(contasC[numero])
                        case default:
                            break
                case 2:
                    opcao = f.menuOperacoes(tipoConta)
                    match opcao:
                        case 1:
                            numero = input(cons.MSG_NUMERO_CONTA)
                            if f.validaTamanhoConta(numero):
                                if f.existeConta(numero, contasP):
                                    valor = int(input(cons.MSG_VALOR_SAQUE))
                                    if f.existeSaldo(numero, contasP, tipoConta, valor):
                                        contasP[numero] -= valor
                                        print(cons.MSG_SUCESSO_SAQUE)
                        case 2:
                            numero = input(cons.MSG_NUMERO_CONTA)
                            if f.existeConta(numero, contasP):
                                valor = int(input(cons.MSG_VALOR_DEPOSITO))
                                contasP[numero] += valor
                                print(cons.MSG_SUCESSO_DEPOSITO)
                        case 3:
                            numero = input(cons.MSG_NUMERO_CONTA)
                            if f.validaTamanhoConta(numero):
                                if f.existeConta(numero, contasP):
                                    numeroContaDestino = input(cons.MSG_NUMERO_CONTA_DESTINO)
                                    tipoDestino = f.validaTipoConta()
                                    match tipoDestino:
                                        case 1:
                                            if f.existeConta(numeroContaDestino, contasC):
                                                valor = int(input(cons.MSG_VALOR_TRANSFERENCIA))
                                                if f.existeSaldo(numero, contasP, tipoConta, valor):
                                                    contasP[numero] -= valor
                                                    contasC[numeroContaDestino] += valor
                                        case 2:
                                            if f.existeConta(numeroContaDestino, contasP):
                                                valor = int(input(cons.MSG_VALOR_TRANSFERENCIA))
                                                if f.existeSaldo(numero, contasP, tipoConta, valor):
                                                    contasP[numero] -= valor
                                                    contasP[numeroContaDestino] += valor
                                        case default:
                                            if f.existeConta(numeroContaDestino, contasS):
                                                valor = int(input(cons.MSG_VALOR_TRANSFERENCIA))
                                                if f.existeSaldo(numero, contasP, tipoConta, valor):
                                                    contasP[numero] -= valor
                                                    contasS[numeroContaDestino] += valor
                                print(cons.MSG_SUCESSO_TRANSFERENCIA)
                        case 4:
                            numero = input(cons.MSG_NUMERO_CONTA)
                            if f.validaTamanhoConta(numero):
                                if f.existeConta(numero, contasP):
                                    print(contasP[numero])
                        case default:
                            break
                case default:
                    opcao = f.menuOperacoes(tipoConta)
                    match opcao:
                        case 1:
                            numero = input(cons.MSG_NUMERO_CONTA)
                            if f.validaTamanhoConta(numero):
                                if f.existeConta(numero, contasS):
                                    valor = int(input(cons.MSG_VALOR_SAQUE))
                                    if f.existeSaldo(numero, contasS, tipoConta, valor):
                                        contasS[numero] -= valor
                        case 2:
                            numero = input(cons.MSG_NUMERO_CONTA)
                            if f.validaTamanhoConta(numero):
                                if f.existeConta(numero, contasS):
                                    print(contasS[numero])
                        case default:
                            pass
        case 5:
            print(cons.MSG_EXIT_SISTEMA)
            f.AguardaLimpa()
            break
        case default:
            print(cons.MSG_OPCAO_INVALIDA)
            f.AguardaLimpa()