from Baralho import Baralho
from PilhaEncadeada import Pilha
from Jogador import Jogador

class Batalha:
    p = Pilha()
    baralho1 = Baralho()
    baralho1.embaralhar()

    cartasBloqueadasPeloEmpate = Pilha()

    def __init__(self):
        self.__rodada = 0

    def getRodada(self):
        return self.__rodada

    def setRodada(self, rodada):
        self.__rodada = rodada

    # Empilha as 52 cartas em p que é a pilha geral
    for i in range(52):
        removido = baralho1.retirarCarta()
        p.empilha(removido)


    #receberCartas 26 vezes cada play
    def distribuirCartas(self, jogador):
        for cont in range(26):
            carta = self.p.desempilha()
            jogador.receberCartas(carta)


    # Retorna o total de cartas
    def imprimirTotalDeCartas(self):
        return f'{self.p.tamanho()}'


    def imprimirCartasBloqueadas(self):
        return f'{self.cartasBloqueadasPeloEmpate}'


    def distribuirCartasBloqueadas(self, jogador):
        jogador.conquistouUmaCarta(self.cartasBloqueadasPeloEmpate.desempilha())


    # Exibe o número da rodada
    def __str__(self):
        return f'Rodada: {self.getRodada()}\n'
