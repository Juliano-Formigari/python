class Veiculo:
    #Atributos
    ano = 2022

    #Métodos da classe
    #Método construtor - Atributos de instância
    def __init__(self, ano, cor, portas, velocidadeMaxima):
        self.ano = ano
        self.cor = cor
        self.portas = portas
        self.velocidadeMaxima = velocidadeMaxima
        self.ligado = False
        self.totalMarchas = 5
        self.marcha = 0
        self.velocidade = 0
        self.mudaMarcha = False

    def ligar(self):
        if self.marcha == 0:
            if not(self.ligado):
                self.ligado = True
                self.mudaMarcha = True
                return 'Carro ligado'
            return 'Carro já está ligado'
        return 'O carro precisar estar no neutro para ligar!'
    
    def desligar(self):
        if self.marcha == 0:
            if(self.ligado):
                self.ligado = False
                self.mudaMarcha = False
                return 'Carro desligado'
            return 'Carro já está desligado'
        return 'O carro precisar estar no neutro para desligar!'
        
    def subirMarcha(self):
        if self.ligado:
            if self.marcha < self.totalMarchas:
                self.marcha += 1
                return 'Está na marcha ' + str(self.marcha)
            return 'Já está na marcha ' + str(self.marcha)
        return 'O carro precisa estar ligado para subir marcha!'

    def descerMarcha(self):
        if self.ligado:
            if self.marcha > -1:
                self.marcha -= 1
                if self.marcha == -1:
                    return 'O carro está na marcha ré!'
                return 'Está na marcha ' + str(self.marcha)
            return 'O carro já está andando de ré'
        return 'O carro precisa estar desligado para subir marcha!'

    def acelarar(self):
        if self.ligado:
            self.velocidade += 20
            if self.velocidade < 21:
                print(self.subirMarcha())
            elif self.velocidade >= 40 and self.velocidade < 60 and self.marcha < 2:
                print(self.subirMarcha())
            elif self.velocidade >= 60 and self.velocidade < 80 and self.marcha < 2:
                print(self.subirMarcha())
            elif self.velocidade >= 80 and self.velocidade <= 100 and self.marcha < 4:
                print(self.subirMarcha())
            elif self.velocidade > 100 and self.velocidade < 120 and self.marcha < 4:
                print(self.subirMarcha())                
            elif self.velocidade < self.VelMaxima and self.velocidade >= 140 and self.marcha < 5:
                print(self.subirMarcha())
            return 'Velocidade atual: ' + str(self.velocidade)
        return 'O carro precisa estar ligado para acelerar'