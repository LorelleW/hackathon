public class Competence():
    def __init__(self,nom:str,niveau:int,description:str,delai:int):
        self.__nom=nom 
        self.__niveau=niveau
        self.__description=description
        self.__delai=delai

    def get_nom(self):
        return self.__nom

    def set_nom(self, nom):
        self.__nom = nom

    def get_niveau(self):
        return self.__niveau

    def set_niveau(self, niveau):
        self.__niveau = niveau

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    def get_delai(self):
        return self.__delai

    def set_delai(self, delai):
        self.__delai = delai
