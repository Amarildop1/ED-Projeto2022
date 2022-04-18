from Carta import Carta
import random

class BaralhoException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class Baralho:
    def __init__(self):
        self.baralho = list()
        naipe = ["Ouro",    "Espada","Paus","Copas"]
        cor =   ["vermelho","preto", "preto","vermelho"]
        numeracao = ["As","2","3","4","5","6","7","8","9","10","valete","dama","rei"]

        for idx in range(len(naipe)):
            for id in numeracao:
                self.baralho.append( Carta(id, naipe[idx], cor[idx]) )


    def __len__(self):
        return len(self.baralho)


    def temCarta(self):
        if len(self.baralho) > 0:
            return True
        else:
            return False


    def retirarCarta(self)->Carta:
        try:
            return self.baralho.pop()
        except IndexError :
            raise BaralhoException('O baralho está vazio. Não há cartas para retirar')


    def embaralhar(self):
        embaralhado = random.shuffle(self.baralho)
        return embaralhado

    """ Para ficar confome o item 2 dos requisitos não-funcionais:
        O código abaixo dentro de um método deve servir pra o requisito.
        O retorno pode ser a pilha pra usar lá em Batalha.py 

        p = Pilha()
        print("Pilha Geral com o baralho: \n")

        #Empilha as 52 cartas em p que é a pilha geral
        for i in range(52):
            removido = baralho1.retirarCarta()
            p.empilha(removido)

        print(p.imprime()) #com esse método exibe None | só com p exibe sem o None
        print(p.tamanho())
    
     """


    def __str__(self):
        saida = ''
        for carta in self.baralho:
            saida += carta.__str__() + '\n' 
        return saida

