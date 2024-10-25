class Echoppe():
    def __init__(self,inventaire,argent,batiment:str,type6:str,proprietaire:str): 
        self.__inventaire=inventaire 
        self.__argent=argent
        self.__batiment=batiment
        self.__type6=type6 
        self.__proprietaire=proprietaire

    def get_inventaire(self):
        return self.__inventaire

    def set_inventaire(self, inventaire):
        self.__inventaire = inventaire

    def get_argent(self):
        return self.__argent

    def set_argent(self, argent):
        self.__argent = argent

    def get_batiment(self):
        return self.__batiment

    def set_batiment(self, batiment):
        self.__batiment = batiment

    def get_type6(self):
        return self.__type6

    def set_type6(self, type6):
        self.__type6 = type6

    def get_proprietaire(self):
        return self.__proprietaire

    def set_proprietaire(self, proprietaire):
        self.__proprietaire = proprietaire
