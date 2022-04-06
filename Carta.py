class Carta:

    def __init__(self, numero, naipe):
        self.__numero = numero
        self.__naipe = naipe


    def __str__(self):
        return f'{self.__numero} de {self.__naipe}'