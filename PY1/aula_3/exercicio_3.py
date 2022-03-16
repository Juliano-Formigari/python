t100 = 0
t50 = 0
t20 = 0
t10 = 0
t5 = 0
t2 = 0
t1 = 0

valorTotal = int(input('Digite um valor inteiro: '))
while(valorTotal >= 100):
    t100 += 1
    valorTotal -= 100
while(valorTotal >= 50):
    t50 += 1
    valorTotal -= 50
while(valorTotal >= 20):
    t20 += 1
    valorTotal -= 20
while(valorTotal >= 10):
    t10 += 1
    valorTotal -= 10
while(valorTotal >= 5):
    t5 += 1
    valorTotal -= 5
while(valorTotal >= 2):
    t2 += 1
    valorTotal -= 2
while(valorTotal >= 1):
    t1 += 1
    valorTotal -= 1

if(t100 != 0 ): 
    print('Total de notas de R$ 100,00  ->      ' + str(t100))
if(t50 != 0 ): 
    print('Total de notas de R$ 50,00   ->      ' + str(t50))
if(t20 != 0 ):
    print('Total de notas de R$ 20,00   ->      ' + str(t20))
if(t10 != 0 ):
    print('Total de notas de R$ 10,00   ->      ' + str(t10))
if(t5 != 0 ):
    print('Total de notas de R$ 5,00    ->      ' + str(t5))
if(t2 != 0 ):
    print('Total de notas de R$ 2,00    ->      ' + str(t2))
if(t1 != 0 ):
    print('Total de notas de R$ 1,00    ->      ' + str(t1))
