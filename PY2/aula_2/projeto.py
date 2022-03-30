from operator import le
from classeContaCorrente import ContaCorrente
from classeContaPoupanca import ContaPoupanca
from classeContaSalario import ContaSalario
import funcoes as f

contasC = [] #Conta Corrente
contasP = [] #Conta Poupança
contasS = [] #Conta Salário

opcao = 0
tipoConta = 0

f.LimpaTela()

while opcao != 4:
    print('Banco PROWAY')
    print('1 - Criar Conta | 2 - Listar Contas | 3 - Excluir Contas | 4 - Sair')
    opcao = int(input('Informe a opção desejada!'))
    f.LimpaTela()

    match opcao:
        case 1:
            tipoConta = f.validaTipoConta()
            f.LimpaTela()
            numero = input('Informe o número da conta!')
            if len(numero) != 5:
                print('Número inválido!')
                f.AguardaLimpa()
            else:
                match tipoConta:
                    case 1:
                        if numero in contasC:
                            print('Conta corrente já existente!')
                        else:
                            contasC.append(numero)
                            print('Conta corrente cadastrada com sucesso')
                    case 2:
                        if numero in contasS:
                            print('Conta salário já existente!')
                        else:
                            contasS.append(numero)
                            print('Conta salário cadastrada com sucesso')
                    case default:
                        if numero in contasP:
                            print('Conta poupança já existente!')
                        else:
                            contasP.append(numero)
                            print('Conta poupança cadastrada com sucesso')
            f.AguardaLimpa()
        case 2:
            tipoConta = f.validaTipoConta()
            f.LimpaTela()
            match tipoConta:
                case 1:
                    if len(contasC) == 0:
                        print('Não há contas correntes cadastradas')
                    else:
                        print(contasC)
                case 2:
                    if len(contasS) == 0:
                        print('Não há contas salários cadastradas')
                    else:
                        print(contasS) 
                case default:
                    if len(contasP) == 0:
                        print('Não há contas poupanças cadastradas')
                    else:
                        print(contasP)
            f.AguardaLimpa()
        case 3:
            tipoConta = f.validaTipoConta()
            f.LimpaTela()
            match tipoConta:
                case 1:
                    if len(contasC) == 0:
                        print('Não há contas correntes cadastradas')
                    else:
                        numero = input('Número da conta que deseja excluir: \n')
                        if len(numero) != 5:
                            print('Número inválido!')
                        else:
                            if not numero in contasC:
                                print('Conta inexistente!')
                            else:
                                contasC.remove(numero)
                                print('Conta excluída com sucesso!')
                case 2:
                    if len(contasS) == 0:
                        print('Não há contas salário cadastradas')
                    else:
                        numero = input('Número da conta que deseja excluir: \n')
                        if len(numero) != 5:
                            print('Número inválido!')
                        else:
                            if not numero in contasS:
                                print('Conta inexistente!')
                            else:
                                contasS.remove(numero)
                                print('Conta excluída com sucesso!')
                case default:
                    if len(contasP) == 0:
                        print('Não há contas poupanças cadastradas')
                    else:
                        numero = input('Número da conta que deseja excluir: \n')
                        if len(numero) != 5:
                            print('Número inválido!')
                        else:
                            if numero in contasP:
                                print('Conta inexistente')
                            else:
                                contasP.remove(numero)
                                print('Conta excluída com sucesso!')
            f.AguardaLimpa()
        case 4:
            print('Obrigado por usar o sistema!')
            f.AguardaLimpa()
            break
        case default:
            print('Opção inválida!')
            f.AguardaLimpa()