valorInteiro = 0
valorTotal = 0

while(valorInteiro != -1):
    valorTotal = valorTotal + valorInteiro
    valorInteiro = int(input("Digite um valor inteiro: "))
print('Soma total = ' + str(valorTotal))