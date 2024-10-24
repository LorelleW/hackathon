public class Livre():
    def __init__(self,nom:str,type7:str,prix:int,effets:str,rarete): 
        self.__nom=nom
        self.__type7=type7
        self.__prix=prix
        self.__effets=effets
        self.__rarete=rarete


# Getter et Setter pour nom
    def get_nom(self):
        return self.__nom

    def set_nom(self, nom):
        self.__nom = nom

    # Getter et Setter pour type7
    def get_type7(self):
        return self.__type7

    def set_type7(self, type7):
        self.__type7 = type7

    # Getter et Setter pour prix
    def get_prix(self):
        return self.__prix

    def set_prix(self, prix):
        self.__prix = prix

    # Getter et Setter pour effets
    def get_effets(self):
        return self.__effets

    def set_effets(self, effets):
        self.__effets = effets

    # Getter et Setter pour rarete
    def get_rarete(self):
        return self.__rarete

    def set_rarete(self, rarete):
        self.__rarete = rarete
