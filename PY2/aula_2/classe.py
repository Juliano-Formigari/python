class Mamifero():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.parado = True

    def mover(self):
        print(self.nome + ' é ' + __class__.__name__ + ' e está se movendo')
        self.parado = False

    def parar(self):
        print(self.nome + ' é ' + __class__.__name__ + ' e está parado')
        self.parado = True

    def comer(self):
        print(self.nome + ' é ' + __class__.__name__ + ' e está comendo')

class Cao(Mamifero):
    def latir(self):
        print(self.nome + ' é ' + __class__.__name__ + ' e está latindo')

class Pessoa(Mamifero):
    def falar(self):
        print(self.nome + ' é ' + __class__.__name__ + ' e está falando')

ser = Cao('totó', 10)
ser.mover()
ser.parar()
ser.latir()
ser = Pessoa('juca', 38)
ser.mover()
ser.parar()
ser.falar()