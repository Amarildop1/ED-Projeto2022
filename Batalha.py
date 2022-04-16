# Classe principal de início do Jogo
from Baralho import Baralho
from PilhaEncadeada import Pilha

if __name__ == "__main__":

    baralho1 = Baralho()
    #print("EM ORDEM: \n")
    #print(baralho1)

    #print("===========================")

    baralho1.embaralhar()
    print("EMBARALHADO: \n")
    print(baralho1)

    print("==========================")


    p = Pilha()

    print("Pilha Geral com o baralho: \n")

    p.empilha(baralho1)

    print(p.imprime())

