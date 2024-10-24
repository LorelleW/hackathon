public class Inventaire():
    def __init__(self,livres,armures,armes,objets): #mettre un système % de chance
        self.__livres=livres
        self.__armures=armures
        self.__armes=armes
        self.__objets=objets

    def get_livres(self):
        return self.__livres

    def set_livres(self, livres):
        self.__livres = livres

    def get_armures(self):
        return self.__armures

    def set_armures(self, armures):
        self.__armures = armures

    def get_armes(self):
        return self.__armes

    def set_armes(self, armes):
        self.__armes = armes

    def get_objets(self):
        return self.__objets

    def set_objets(self, objets):
        self.__objets = objets

