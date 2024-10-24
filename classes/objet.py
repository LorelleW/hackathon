public class Objet():
    def __init__(self,nom:str,type3:str,prix:int,materiaux:str,rarete:str): 
        self.__nom=nom 
        self.__type3=type3
        self.__prix=prix
        self.__materiaux=materiaux
        self.__rarete=rarete


    def get_nom(self):
        return self.__nom

    def set_nom(self,nom):
        self.__nom=nom

    def get_type3(self):
        return self.__type3

    def set_type3(self,type3):
        self.__type3=type3

    def get_prix(self):
        return self.__prix

    def set_prix(self,prix):
        self.__prix=prix

    def get_materiaux(self):
        return self.__materiaux

    def set_materiaux(self,materiaux):
        self.__materiaux=materiaux

    def get_rarete(self):
        return self.__rarete

    def set_rarete(self,rarete):
        self.__rarete=rarete
