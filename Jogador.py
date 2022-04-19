from PilhaEncadeada import Pilha

class Jogador:
    """ Classe que representa um Jogador.

        Métodos:

        getQtdeCartasNaMao(self):
            Retorna a quantidade de cartas na mão do jogador.

        getTotalDeCartas(self):
            Retorna a quantidade total de cartas do jogador, considerando as que ele ganhou.
        
        puxarCarta(self):
            Retorna a carta puxada pelo jogador.
        receberCartas(self, carta):
            Adiciona as cartas em uma pilha do jogador.

        conquistouUmaCarta(self, carta):
            Adiciona cartas recebidas após ganhar uma rodada.
    """
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
        """  Retorna a carta puxada pelo jogador. """
        puxou = self.pilhaPlayer.desempilha()
        self.cartasNaMao -= 1
        self.totalDeCartas -= 1
        return puxou


    def receberCartas(self, carta):
        """ Adiciona as cartas em uma pilha do jogador. """
        self.pilhaPlayer.empilha(carta)
        self.cartasNaMao += 1
        self.totalDeCartas += 1


    def conquistouUmaCarta(self, carta):
        """ Adiciona cartas recebidas após ganhar de outro jogador. """
        self.pilhaDeCartasConquistadas.empilha(carta)
        self.totalDeCartas += 1


    def perdeuUmaCarta(self):
        self.totalDeCartas -= 1


    def __str__(self):
        return f'Jogador: {self.getNome()} \nTotal de cartas: {self.getTotalDeCartas()}\n\nCartas na Mao: \n{self.pilhaPlayer}\n \nCartas conquistadas: {self.pilhaDeCartasConquistadas}\n'
