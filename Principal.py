# Arquivo principal de início do Jogo
from PilhaEncadeada import Pilha
from Jogador import Jogador
from Batalha import Batalha


# Definindo os 2 Jogadores
play1 = Jogador("Player 1")
play2 = Jogador("Player 2")


def informacaoSobreOjogo():
    print("\n\n - - - - INFORMAÇÕES SOBRE O JOGO - - - - ")
    print("""
> Para iniciar o jogo: Digite 1
> Nome padrão dos jogadores: Player 1 e Player 2
> Caso queira mudar os nomes: Digite 2 no menu
> Para Sair e encerrar o jogo: Digite o 0 no menu\n
:) Versão 1.0 - 2022
    """)


def revelarCampeao():
    if ( play1.getTotalDeCartas() > play2.getTotalDeCartas() ):
        return f'{play1.getNome()} VENCEU A BATALHA!'
    if ( play1.getTotalDeCartas() < play2.getTotalDeCartas() ):
        return f'{play2.getNome()} VENCEU A BATALHA!'
    else:
        return f'HOUVE EMPATE ENTRE OS JOGADORES'


# FUNÇÃO INICIAR JOGO
def iniciarJogo():
    print("\n\n\n * * * * * * * * * * * * INICIO DO JOGO * * * * * * * * * * * * \n")

    # Criando a Batalha/Mesa
    batalha1 = Batalha()


    # Total de cartas antes da distribuição
    print(f'TOTAL DE CARTAS DO JOGO: {batalha1.imprimirTotalDeCartas()}\n')


    # Definindo os 2 Jogadores
    #play1 = Jogador("Player 1")
    #play2 = Jogador("Player 2")

    # Jogadores que estão na disputa
    print(f'Jogadores(as):  {play1.getNome()}  vs  {play2.getNome()}')

    # Distribuição das cartas para os Jogadores | Mão de carta de cada
    batalha1.distribuirCartas(play1)
    batalha1.distribuirCartas(play2)


    print(f'\n{play1}')
    print(" . . . . . . . . . . . . . . . . . . . . ")
    print(f'\n{play2}')


    ###########################################################################
    #print(" ####################  ATE AQUI TA OK  #################### \n") ###
    ###########################################################################


    # Se passar de 26 vai mostrar a exceção de pilha vazia
    ######################################################
    for cont in range(5):
        batalha1.setRodada(cont + 1)
        print(f'\n- - - - - - - - - - - - - - - RODADA {batalha1.getRodada()}: - - - - - - - - - - - - - - -\n')

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
                return f'\n - - - - - - - ->  \o/  {play1.getNome()}  GANHOU \o/  <- - - - - - - -\n\n'
            if( self.getNumero() < other.getNumero() ):
                play2.conquistouUmaCarta(mesa.desempilha())
                play2.conquistouUmaCarta(mesa.desempilha())
                if not batalha1.cartasBloqueadasPeloEmpate.estaVazia():
                    batalha1.distribuirCartasBloqueadas(play2)
                    batalha1.distribuirCartasBloqueadas(play2)
                return f'\n - - - - - - - ->  \o/  {play2.getNome()}  GANHOU \o/  <- - - - - - - -\n\n'
            else:
                batalha1.cartasBloqueadasPeloEmpate.empilha(mesa.desempilha())
                batalha1.cartasBloqueadasPeloEmpate.empilha(mesa.desempilha())
                return f'\n\n  EMPATE | AS CARTAS SÃO IGUAIS \n\n'
            # EM CASO DE EMPATE TEM QUE IR BLOQUEANDO AS CARTAS
            # ASSIM QUE ALGUM PLAYER LANÇAR UMA CARTA E DESEMPATAR,
            # ELE RECEBERÁ AS CARTAS BLOQUEADAS.

        print(__cmp__(play1Retirou, play2Retirou))

        if not batalha1.cartasBloqueadasPeloEmpate.estaVazia():
            print(f'Cartas Bloqueadas por empate: {batalha1.imprimirCartasBloqueadas()}\n')

        print(f'Cartas Conquistadas por {play1.getNome()}:\n {play1.pilhaDeCartasConquistadas}')
        print(f'\nCartas Conquistadas por {play2.getNome()}:\n {play2.pilhaDeCartasConquistadas}')

        print(f'\nTotal de cartas de {play1.getNome()}: {play1.getTotalDeCartas()}')
        print(f'Total de cartas de {play2.getNome()}: {play2.getTotalDeCartas()}')

        print(f'- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n\n')


    # DEFININDO O CAMPEÃO
    print(f'\t \o/  {revelarCampeao()}  \o/ \n')

    print(f'\nTotal final: {play1.getTotalDeCartas()} cartas com {play1.getNome()}')
    print(f'\nTotal final: {play2.getTotalDeCartas()} cartas com {play2.getNome()}')

    print("\n\nINFORME UM NÚMERO SE DESEJAR JOGAR NOVAMENTE.")
######################################################################################


# SE PRESSIONAR ENTER SEM NÚMERO DE OPERAÇÃO DÁ EXCEÇÃO: 
#ValueError: invalid literal for int() with base 10: 'g'
# SE PRESSIONAR ALGUMA LETRA DÁ EXCEÇÃO: 
#ValueError: invalid literal for int() with base 10: 'h'
#SE APÓS UM VENCEDOR, O USER ESCOLHER 1 PARA INICIAR OUTRA PARTIDA, A PILHA ESTARÁ VAZIA
#DÁ A EXCEÇÃO DE PILHA VAZIA

def mostrarMenu(): 
    escolha = True

    while escolha != 0 :
        print("\n\n- - - - - - - - - MENU - - - - - - - - -")
        print("\n [1] Iniciar partida")
        print(" [2] Escolher nome do Jogador")
        print(" [3] Informações")
        print(" [0] Sair")
        try:
            escolha = int(input("\nInforme o número da operação desejada: "))
            print("- - - - - - - - - - - - - - - - - - - - -")
            if escolha == 1:
                iniciarJogo()
            elif escolha == 2:
                play1.setNome(input("\nInforme o nome do Jogador 1: "))
                play2.setNome(input("Informe o nome do Jogador 2: "))
                print("\nNOMES SALVOS COM SUCESSO!!! Pode iniciar o jogo. ")
            elif escolha == 3:
                informacaoSobreOjogo()
            elif escolha == 0:
                print("\nFIM DE JOGO. Bye!\n")
            else:
                print("\n\n:/ Ops! Digite um número de operação válido. ;)")
        except ValueError:
            print("\n\nINFORME UM NÚMERO INTEIRO E VÁLIDO DISPONÍVEL NO MENU <-----")


########################## P R I N C I P A L ##########################

if __name__ == "__main__":

    print("\n # # # # # # # # # # JOGO BATALHA DE CARTAS # # # # # # # # # #")
    mostrarMenu()
