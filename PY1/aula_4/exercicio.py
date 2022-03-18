from email.policy import default
import controller
import os

os.system('cls')
print('WELCOME TO PAGE TOP SYSTEM PROWAY')


opcao = int(input('1 - Cadastrar | 2 - Alterar | 3 - Visualizar | 4 - Excluir'))

match opcao:
        case 1:
            controller.cadastrar()
        case default:
            print('Opção inválida!')



