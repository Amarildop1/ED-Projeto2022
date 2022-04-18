from PilhaEncadeada import Pilha

class Jogador:
    cartasNaMao = 0
    totalDeCartas = 0

    def __init__(self, nome):
        self.pilhaPlayer = Pilha()
        self.__nome = nome
        self.pilhaDeCartasConquistadas = Pilha()


    def getNome(self):
        return self.__nome
    
    def setNome(self, novoNome):
        self.__nome = novoNome


    def getQtdeCartasNaMao(self):
        return self.cartasNaMao


    def getTotalDeCartas(self):
        return self.totalDeCartas


    def puxarCarta(self):
        puxou = self.pilhaPlayer.desempilha()
        self.cartasNaMao -= 1
        self.totalDeCartas -= 1
        return puxou


    def receberCartas(self, carta):
        self.pilhaPlayer.empilha(carta)
        self.cartasNaMao += 1
        self.totalDeCartas += 1


    def conquistouUmaCarta(self, carta):
        self.pilhaDeCartasConquistadas.empilha(carta)
        self.totalDeCartas += 1


    def perdeuUmaCarta(self):
        self.totalDeCartas -= 1


    def __str__(self):
        return f'Jogador: {self.getNome()} \nTotal de cartas: {self.getTotalDeCartas()}\n\nCartas na Mao: \n{self.pilhaPlayer}\n \nCartas conquistadas: {self.pilhaDeCartasConquistadas}\n'
