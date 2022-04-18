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
    batalha1 = Batalha()

    # Total de cartas antes da distribuição
    print(f'{batalha1.imprimirTotalDeCartas()}\n')


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



    ######################################################
    for cont in range(5):
        batalha1.setRodada(cont + 1)
        print(f'. . . . . . . . . . . . . RODADA {batalha1.getRodada()}: . . . . . . . . . . . . .')

        # Mostrando a quantidade de cartas na mão do jogador
        print(f'Cartas na mao de play1: {play1.getQtdeCartasNaMao()}')
        print(f'Cartas na mao de play2: {play2.getQtdeCartasNaMao()}')

        # Play1 e Play2 retiram as cartas
        play1Retirou = play1.puxarCarta()
        play2Retirou = play2.puxarCarta()
        print(f'\nPlay1 tirou: {play1Retirou}   vs   Play2 tirou: {play2Retirou}')


        mesa = Pilha()
        mesa.empilha(play1Retirou)
        mesa.empilha(play2Retirou)
        #print(f'Cartas na mesa: {mesa}')



        #AINDA NÃO ESTÁ CERTO
        #AS VITÓRIAS NÃO ESTÃO SEMPRE OK
        def __cmp__(self, other):
            if( self.getNumero() > other.getNumero() ):
                play1.conquistouAsCartas(mesa.desempilha())
                play1.conquistouAsCartas(mesa.desempilha())
                print(f'Conquistadas: {play1.pilhaDeCartasConquistadas}')
                return "PLAY1 VENCE \o/ \n"
            elif( self.getNumero() < other.getNumero() ):
                play2.pilhaDeCartasConquistadas.empilha(mesa.desempilha())
                play2.pilhaDeCartasConquistadas.empilha(mesa.desempilha())
                return f'PLAY2 VENCE \o/ \n'
            else:
                batalha1.cartasBloqueadasPeloEmpate.empilha(mesa.desempilha())
                batalha1.cartasBloqueadasPeloEmpate.empilha(mesa.desempilha())
                return f'EMPATE \n'
            # EM CASO DE EMPATE TEM QUE IR BLOQUEANDO AS CARTAS
            # ASSIM QUE ALGUM PLAYER LANÇAR UMA CARTA E DESEMPATAR, 
            # ELE RECEBERÁ AS CARTAS BLOQUEADAS E ADICIONA EMBAIXO DO SEU MONTE


        print(__cmp__(play1Retirou, play2Retirou))

        print(f'Cartas Bloqueadas: {batalha1.imprimirCartasBloqueadas()}\n\n')

        print(f'. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n')

    
    print(f'\n{play1}')
    print(f'\n{play2}')
    ######################################################




    #DAQUI PRA BAIXO É TESTE
    #A mesa vai ser uma pilha

    """ # Play1 e Play2 retiram as cartas
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


    print(__cmp__(play1Retirou, play2Retirou)) """