class Carta:

    def __init__(self, numero, naipe, cor):
        self.__numero = numero
        self.__naipe = naipe
        self.__cor = cor


    def __str__(self):
        return f'{self.__numero} de {self.__naipe}'