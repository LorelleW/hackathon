class Competence():
    def __init__(self,nom:str,niv:int,attaque:int,defense:int,degat:int,soin:int,delai:int,effet:int):
        self.__nom=nom 
        self.__niv=niv
        self.__delai=delai
        self.__attaque=attaque
        self.__defense=defense
        self.__degat=degat
        self.__soin=soin
        self.__delai=delai
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

    def get_attaque(self):
        return self.__attaque

    def set_attaque(self,attaque):
        self.__attaque=attaque

    def get_defense(self):
        return self.__defense

    def set_defense(self,defense):
        self.__defense=defense

    def get_degat(self):
        return self.__degat

    def set_degat(self,degat):
        self.__degat=degat

    def get_soin(self):
        return self.__soin

    def set_soin(self,soin):
        self.__soin = soin

    def get_delai(self):
        return self.__delai

    def set_delai(self,delai):
        self.__delai=delai
        
    
    def get_effet(self):
        return self.__soin

    def set_effet(self,effet):
        self.__effet=effet
        
