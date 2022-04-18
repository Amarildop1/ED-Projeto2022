from PilhaEncadeada import Pilha

class Jogador:

    def __init__(self, nome):
        self.pilhaPlayer = Pilha()
        self.__nome = nome


    def getNome(self):
        return self.__nome


    def puxarCarta(self):
        puxou = self.pilhaPlayer.desempilha()
        return puxou


    def receberCartas(self, carta):
        self.pilhaPlayer.empilha(carta)


    def __str__(self):
        return f'Jogador: {self.getNome()} \nSuas cartas: \n{self.pilhaPlayer}\n'
