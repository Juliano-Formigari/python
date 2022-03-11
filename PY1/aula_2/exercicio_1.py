from email.policy import default


nome = input("Informe seu nome: ")
genero = int(input("Selecione seu genêro: [1 - Masculino | 2 - Feminino]"))

match genero:
    case 1:
        idade = int(input("Digite sua idade: "))
        match idade:
            case 18:
                print("CONVOCADO")
            case default:
                print("DISPENSADO")
    case default:
        print("DISPENSADO")
