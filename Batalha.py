from Baralho import Baralho
from PilhaEncadeada import Pilha

class Batalha:
    """ Classe que representa uma batalha/jogo.

        Variáveis:
            p: Do tipo Pilha.
            cartasBloqueadasPeloEmpate: Do tipo Pilha.
            baralho1: Do tipo Baralho.

        Métodos:

        distribuirCartas(self, jogador): 
            Faz a distribuição de cartas para um Jogador.
        imprimirTotalDeCartas(self): 
            Retorna o total de cartas de um Jogador.
        imprimirCartasBloqueadas(self): 
            Retorna as cartas bloqueadas pelo empate
        distribuirCartasBloqueadas(self, jogador): 
            Faz a distribuição das cartas bloqueadas
    """
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
        """ Método para distribuir 26 cartas para o jogador.

            Recebe um Parâmetro: O Jogador que receberá as cartas.

            Não há retorno.

            Invoca o método de receber cartas do jogador recebido no parâmetro.
        """
        for cont in range(26):
            carta = self.p.desempilha()
            jogador.receberCartas(carta)


    # Retorna o total de cartas com base no tamanho da pilha p
    def imprimirTotalDeCartas(self):
        return f'{self.p.tamanho()}'


    def imprimirCartasBloqueadas(self):
        """ Retorna as cartas bloqueadas. """
        return f'{self.cartasBloqueadasPeloEmpate}'


    def distribuirCartasBloqueadas(self, jogador):
        """ Método para distribuir a cartas bloqueadas.

            Recebe um Parâmetro: O Jogador que receberá as cartas.

            Não há retorno.

            Invoca o método de conquistar cartas do jogador recebido no parâmetro.
        """
        jogador.conquistouUmaCarta(self.cartasBloqueadasPeloEmpate.desempilha())


    # Exibe o número da rodada
    def __str__(self):
        """ Retorna um número inteiro que representa a rodada atual. """
        return f'Rodada: {self.getRodada()}\n'
