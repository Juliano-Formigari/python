
etanol = 4.689
gasolinaAditivada = 7.099
gasolinaComum = 5.899
diesel = 4.599

name = input("Informe seu nome: ")
selectOption = int(input("Selecione a opção: [1-Valor | 2-Litros] \n\n"))
typeFuel = int(input("Selecione o tipo de combustível: [1-ETANOL | 2-GASOLINA ADITIVA | 3-GASOLINA COMUM | 4-DIESEL"))

match selectOption:
    case 1:
        value = float(input("Digite o valor: "))
        match typeFuel:
            case 1:
                print("Volume em litros:" + str(value / etanol) + " litros")
            case 2:
                print("Volume em litros:" + str(value / gasolinaAditivada) + " litros")
            case 3:
                print("Volume em litros:" + str(value / gasolinaComum) + " litros")
            case 4:
                print("Volume em litros:" + str(value / diesel) + " litros")
            case default:
                print("Opção invalida!")
    case default:
        print("Opção invalida!")
match selectOption:
    case 2:
        value = float(input("Digite o valor: "))
        match typeFuel:
            case 1:
                print("Valor a pagar: R$ " + str(value * etanol))
            case 2:
                print("Valor a pagar: R$" + str(value * gasolinaAditivada))
            case 3:
                print("Valor a pagar: R$" + str(value * gasolinaComum))
            case 4:
                print("Valor a pagar: R$" + str(value * diesel))
            case default:
                print("Opção invalida!")
    case default:
        print("Opção invalida!")
