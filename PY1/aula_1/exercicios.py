nome = input("Digite seu nome: ")
anoNascimento = int(input("Que ano você nasceu??\n"))
anoAtual = 2022
idadeMinima = anoAtual - 2004

if(anoAtual - anoNascimento >= 18):
    print("Piloto " + nome + " com permissão para dirigir!")
else:
    print("Piloto " + nome + " sem permissão para digirir!" )
    print("Precisa aguardar: " + str(idadeMinima - (anoAtual - anoNascimento)) + " anos")
