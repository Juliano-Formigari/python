numA = int(input("Digite o primeiro valor: "))
operacao = input("\nSelecione a operação: \n\n [ + | - | * | / ]\n\n\n")
numB = int(input("Digite o segundo valor: "))


match operacao:
    case "+":
        print("Soma = " + str(numA+numB))
    case "-":
        print("Subtração = " + str(numA-numB))
    case "*":
        print("Multiplicação = " + str(numA*numB))
    case "/":
        if(numB == 0):
            print("Impossível dividir por zero!!!")
        else:
            print("Divisão = " + str(numA/numB))
    case default:
        print("Operação inválida, execute de novo e selecione uma opção válida!")