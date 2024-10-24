class Classe():
    def __init__(self,nom:str,caracteristique,type2):
        self.__nom=nom 
        self.__caracteristique=caracteristique
        self.__type2=type2

    def get_nom(self):
        return self.__nom

    def set_nom(self,nom):
        self.__nom=nom

    def get_caracteristique(self):
        return self.__caracteristique

    def set_caracteristique(self,caracteristique):
        self.__caracteristique=caracteristique

    def get_type2(self):
        return self.__type2

    def set_type2(self,type2):
        self.__type2=type2
        
        
        
        
