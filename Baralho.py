from Carta import Carta
import random

class BaralhoException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class Baralho:
    """ Classe que representa um baralho.
    
        Utiliza objetos do tipo Carta:
            Com naipe, cor e numeração.

        Métodos:

        temCarta(self):
            Retorna True ou False em caso de conter cartas ou não.

        retirarCarta(self) -> Carta:
            Retorna uma carta retirada do baralho.

        embaralhar(self):
            Usado para embaralhar o baralho.
    """

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
        """ Método que verifica se há cartas no Baralho.

            Retorna True ou False.
        """
        if len(self.baralho) > 0:
            return True
        else:
            return False


    def retirarCarta(self)->Carta:
        """ Método para retirar carta do baralho.

            Retorna a carta retirada.
                Retorno do tipo Carta.

            Exceção que pode gerar:
                IndexError
        """
        try:
            return self.baralho.pop()
        except IndexError :
            raise BaralhoException('O baralho está vazio. Não há cartas para retirar')


    def embaralhar(self):
        """ Método para embaralhar um baralho comum

            Retorna o baralho com as cartas embaralhadas.

            Faz uso de um método do módulo random.
        """
        embaralhado = random.shuffle(self.baralho)
        return embaralhado


    def __str__(self):
        saida = ''
        for carta in self.baralho:
            saida += carta.__str__() + '\n' 
        return saida

