class Carta:

    def __init__(self, numero, naipe, cor):
        self.__numero = numero
        self.__naipe = naipe
        self.__cor = cor

    def get_numero(self):
        return self.__numero
    
    def get_naipe(self):
        return self.__naipe


    def __str__(self):
        return f'{self.get_numero()} de {self.get_naipe()}'