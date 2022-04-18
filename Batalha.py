from Baralho import Baralho
from PilhaEncadeada import Pilha
from Jogador import Jogador

class Batalha:
    p = Pilha()
    baralho1 = Baralho()
    baralho1.embaralhar()

    def __init__(self, rodada):
        self.__rodada = rodada

    def getRodada(self):
        return self.__rodada


    # Empilha as 52 cartas em p que é a pilha geral
    for i in range(52):
        removido = baralho1.retirarCarta()
        p.empilha(removido)


    #receberCartas 26 vezes cada play
    def distribuirCartas(self, jogador):
        for cont in range(26):
            carta = self.p.desempilha()
            jogador.receberCartas(carta)

    
    def imprimirTotalDeCartas(self):
        return f'TOTAL DE CARTAS: {self.p.tamanho()}'

    # Exibe o número da rodada
    def __str__(self):
        return f'Rodada: {self.getRodada()}\n'
