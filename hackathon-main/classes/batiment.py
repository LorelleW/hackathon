class Batiment():
    def __init__(self,nom:str,age:int,architecture,proprietaire,context_h):
        self.__nom=nom
        self.__age=age
        self.__architecture=architecture
        self.__proprietaire=proprietaire
        self.__context_h=context_h

    def get_nom(self):
        return self.__nom

    def set_nom(self,nom):
        self.__nom=nom

    def get_age(self):
        return self.__age

    def set_age(self,age):
        self.__age=age

    def get_architecture(self):
        return self.__architecture

    def set_architecture(self,batiment):
        self.__architecture=architecture

    def get_proprietaire(self):
        return self.__proprietaire

    def set_proprietaire(self,proprietaire):
        self.__proprietaire=proprietaire

    def get_context_h(self):
        return self.__context_h
    def set_context_h(self,context_h):
        self.__context_h=context_h
        
        
        
