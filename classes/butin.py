class Butin():
    def __init__(self,livre,armure,arme,objet,argent:int): #mettre un système % de chance
        self.__livre=livre
        self.__armure=armure
        self.__arme=arme
        self.__objet=objet
        self.__argent=argent

    def get_livre(self):
        return self.__livre

    def set_livre(self,livre):
        self.__livre=livre

    def get_armure(self):
        return self.__armure

    def set_armure(self,armure):
        self.__armure=armure

    def get_arme(self):
        return self.__arme

    def set_arme(self,arme):
        self.__arme=arme

    def get_objet(self):
        return self.__objet

    def set_objet(self,objet):
        self.__objet=objet

    def get_argent(self):
        return self.__argent

    def set_argent(self,argent):
        self.__argent=argent
        
        
        
        
        
