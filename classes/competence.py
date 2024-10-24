class Competence():
    def __init__(self,nom:str,niv:int,attaque:int,defense:int,degat:int,soin:int,effet:int,delai:int):
        self.__nom=nom 
        self.__niv=niv
        self.__description=description
        self.__delai=delai
        self.__attaque=attaque
        self.__defense=defense
        self.__degat=degat
        self.__soin=soin
        self.__effet=effet

    def get_nom(self):
        return self.__nom

    def set_nom(self, nom):
        self.__nom = nom

    def get_niv(self):
        return self.__niv

    def set_niv(self, niv):
        self.__niv = niv

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    def get_delai(self):
        return self.__delai

    def set_delai(self, delai):
        self.__delai = delai
