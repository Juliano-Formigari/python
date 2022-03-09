

numA = int(input("Digite o primeiro valor inteiro: "))
operador = input("Digite uma das operações: (+ | - | * | /) ")
numB = int(input("Digite o primeiro valor inteiro: "))

#Soma
'''
print('Soma = '             + str((numA+numB)))
print('subtracao = '        + str((numA-numB)))
print('multiplicacao = '    + str((numA*numB)))
print('divisao = '          + str((numA/numB)))'''


if(operador == "+"):
    print(str(numA + numB))
elif(operador == "-"):
    print(str(numA-numB))
elif(operador == "*"):
    print(str(numA*numB))
elif(operador == "/"):
    print(str(numA/numB))
else:
    print("Operação inválida!")


