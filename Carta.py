class Carta:

    def __init__(self, numero, naipe, cor):
        self.__numero = numero
        self.__naipe = naipe
        self.__cor = cor

    def getNumero(self):
        return self.__numero
    
    def getNaipe(self):
        return self.__naipe

    def getCor(self):
        return self.__cor

    def __str__(self):
        return f'{self.getNumero()} de {self.getNaipe()}'