
from decimal import DivisionByZero


try:
    try:
        vl1 = int(input('Informe um valor inteiro: '))
        try:
            vl2 = int(input('Informe outro valor inteiro: '))
            try:
                print('O resultado da divisão dos valores é ' + str(vl1 / vl2))
                print('Obrigado por usar nosso sistema')
            except:
                print('Impossível dividir por zero.')
        except NameError:
            print('Alguma variável não existe!')
        except ZeroDivisionError:
            print('Impossível dividir por zero.')
        except ValueError:
            print('Algum valor inválido foi passado')
        except TypeError:
            print('Tipo de dado inválido!')
        except:
            print('Erro ao informar o segundo valor.')
    except:
        print('Erro ao informar o primeiro valor.')
except:
    print('Erro ao efetuar a divisão')

pais = "Brasil"
print(pais, "Welcome", "Hello", sep='-')