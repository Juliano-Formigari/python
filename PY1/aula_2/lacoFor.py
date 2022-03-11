tabuada = int(input("Informe qual tabuada: "))

for valor1 in range(tabuada, 11):
    print("\nTabuada de " + str(valor1) + "\n")
    for valor2 in range(1 , 11):
        print(str(valor1) + " x " + str(valor2) + " =  " + str(valor1*valor2))