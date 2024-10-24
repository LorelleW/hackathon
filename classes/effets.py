public class Effets():
    def __init__(self,nom:str,description:str):
        self.__nom=nom 
        self.__description=description

    def get_nom(self):
        return self.__nom

    def set_nom(self, nom):
        self.__nom = nom

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description
