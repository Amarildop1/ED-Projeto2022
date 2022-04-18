# Arquivo principal de início do Jogo
from Baralho import Baralho
from PilhaEncadeada import Pilha
from Jogador import Jogador
from Batalha import Batalha


if __name__ == "__main__":
    """
        Iniciar o jogo definindo os jogadores e 
        sua mão de cartas. 
        As cartas devem estar embaralhadas antes da distribuição.
    """

    print("\n - - - - - - - - INICIO DO JOGO - - - - - - - - \n")

    # Criando a Batalha/Mesa
    batalha1 = Batalha("# 01")

    # Total de cartas antes da distribuição
    print(f'{batalha1.imprimirTotalDeCartas()}')

    # Mostrando número da rodada
    print(f'\n{batalha1}')

    # Definindo os 2 Jogadores
    play1 = Jogador("Amarildo")
    play2 = Jogador("Joana")

    # Jogadores que estão na disputa
    print(f'Jogadores(as):  {play1.getNome()}  vs  {play2.getNome()}')

    # Distribuição das cartas para os Jogados | Mão de carta de cada
    batalha1.distribuirCartas(play1)
    batalha1.distribuirCartas(play2)

    print(f'\n{play1}')
    print(f'\n{play2}')


    # # # # # # ATÉ AQUI OK # # # # # #

    #################################################################
    print(" * * * * * * * * * * ATE AQUI TA OK * * * * * * * * * * \n") ################
    #################################################################


    #DAQUI PRA BAIXO É TESTE
    #A mesa vai ser uma pilha

    # Play1 e Play2 retiram as cartas
    play1Retirou = play1.puxarCarta()
    play2Retirou = play2.puxarCarta()
    print(f'Play1 tirou: {play1Retirou}   vs   Play2 tirou: {play2Retirou}\n')


    #AINDA NÃO ESTÁ CERTO
    #AS VITÓRIAS NÃO ESTÃO SEMPRE OK
    def __cmp__(self, other):
        if( self.getNumero() > other.getNumero() ): 
            return "PLAY1 VENCE"
        elif( self.getNumero() < other.getNumero() ): 
            return "PLAY2 VENCE"

        return "EMPATE"
        # EM CASO DE EMPATE TEM QUE IR BLOQUEANDO AS CARTAS
        # ASSIM QUE ALGUM PLAYER LANÇAR UMA CARTA E DESEMPATAR, 
        # ELE RECEBERÁ AS CARTAS BLOQUEADAS E ADICIONA EMBAIXO DO SEU MONTE


    print(__cmp__(play1Retirou, play2Retirou))