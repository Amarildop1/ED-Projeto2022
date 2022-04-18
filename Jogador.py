from PilhaEncadeada import Pilha

class Jogador:
    cartasNaMao = 0

    def __init__(self, nome):
        self.pilhaPlayer = Pilha()
        self.__nome = nome
        self.pilhaDeCartasConquistadas = Pilha()


    def getNome(self):
        return self.__nome


    def getQtdeCartasNaMao(self):
        return self.cartasNaMao


    def puxarCarta(self):
        puxou = self.pilhaPlayer.desempilha()
        self.cartasNaMao -= 1
        return puxou


    def receberCartas(self, carta):
        self.pilhaPlayer.empilha(carta)
        self.cartasNaMao += 1


    def conquistouAsCartas(self, carta):
        self.pilhaDeCartasConquistadas.empilha(carta)


    def __str__(self):
        return f'Jogador: {self.getNome()} \nCartas na Mao: \n{self.pilhaPlayer}\n \nConquistadas: {self.pilhaDeCartasConquistadas}\n'
