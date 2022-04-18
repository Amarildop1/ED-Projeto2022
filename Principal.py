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

    print("\n * * * * * * * * * * * * INICIO DO JOGO * * * * * * * * * * * * \n")

    # Criando a Batalha/Mesa
    batalha1 = Batalha()

    # Total de cartas antes da distribuição
    print(f'TOTAL DE CARTAS DO JOGO: {batalha1.imprimirTotalDeCartas()}\n')


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

    ###########################################################################
    print(" ####################  ATE AQUI TA OK  #################### \n") #############
    ###########################################################################


    # Se passar de 26 vai mostrar a exceção de pilha vazia
    ######################################################
    for cont in range(5):
        batalha1.setRodada(cont + 1)
        print(f'- - - - - - - - - - - - - - - RODADA {batalha1.getRodada()}: - - - - - - - - - - - - - - -\n')

        # Mostrando a quantidade de cartas na mão do jogador
        print(f'Cartas na mao de {play1.getNome()}: {play1.getQtdeCartasNaMao()}   xXx   Cartas na mao de {play2.getNome()}: {play2.getQtdeCartasNaMao()}')
        #print(f'Cartas na mao de play2: {play2.getQtdeCartasNaMao()}')

        # Play1 e Play2 retiram as cartas
        play1Retirou = play1.puxarCarta()
        play2Retirou = play2.puxarCarta()
        print(f'\n{play1.getNome()} tirou: {play1Retirou}   vs   {play2.getNome()} tirou: {play2Retirou}')


        mesa = Pilha()
        mesa.empilha(play1Retirou)
        mesa.empilha(play2Retirou)
        #print(f'Cartas na mesa: {mesa}')


        #AINDA NÃO ESTÁ CERTO
        #AS VITÓRIAS NÃO ESTÃO SEMPRE OK
        def __cmp__(self, other):
            if( self.getNumero() > other.getNumero() ):
                play1.conquistouUmaCarta(mesa.desempilha())
                play1.conquistouUmaCarta(mesa.desempilha())
                if not batalha1.cartasBloqueadasPeloEmpate.estaVazia():
                    batalha1.distribuirCartasBloqueadas(play1)
                    batalha1.distribuirCartasBloqueadas(play1)
                return f'\n - - - - - - - -> \o/ {play1.getNome()} VENCEU \o/ <- - - - - - - -\n\n'
            if( self.getNumero() < other.getNumero() ):
                play2.conquistouUmaCarta(mesa.desempilha())
                play2.conquistouUmaCarta(mesa.desempilha())
                if not batalha1.cartasBloqueadasPeloEmpate.estaVazia():
                    batalha1.distribuirCartasBloqueadas(play2)
                    batalha1.distribuirCartasBloqueadas(play2)
                return f'\n - - - - - - - -> \o/ {play2.getNome()} VENCEU \o/ <- - - - - - - -\n\n'
            else:
                batalha1.cartasBloqueadasPeloEmpate.empilha(mesa.desempilha())
                batalha1.cartasBloqueadasPeloEmpate.empilha(mesa.desempilha())
                return f'\n\n @@ @@ @@ @@ @@ @@ EMPATE EMPATE EMPATE @@ @@ @@ @@ @@ @@ \n\n'
            # EM CASO DE EMPATE TEM QUE IR BLOQUEANDO AS CARTAS
            # ASSIM QUE ALGUM PLAYER LANÇAR UMA CARTA E DESEMPATAR,
            # ELE RECEBERÁ AS CARTAS BLOQUEADAS E ADICIONA EMBAIXO DO SEU MONTE.

        print(__cmp__(play1Retirou, play2Retirou))

        print(f'Cartas Bloqueadas: {batalha1.imprimirCartasBloqueadas()}\n')

        print(f'Cartas Conquistadas por {play1.getNome()}:\n {play1.pilhaDeCartasConquistadas}')
        print(f'\nCartas Conquistadas por {play2.getNome()}:\n {play2.pilhaDeCartasConquistadas}')

        print(f'\nTotal de cartas de {play1.getNome()}: {play1.getTotalDeCartas()}')
        print(f'Total de cartas de {play2.getNome()}: {play2.getTotalDeCartas()}')

        print(f'- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n\n')


    print(f'\n{play1}')
    print(f'\n{play2}')
    ######################################################

