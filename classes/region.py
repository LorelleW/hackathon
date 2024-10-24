class Region():
    def __init__(self,typedelieu,topographie,population,position,proprietaire:str):
        self.__typedelieu=typedelieu
        self.__topographie=topographie
        self.__population=population
        self.__position=position
        self.__proprietaire=proprietaire

#getter
    def get_typedelieu(self):
        return self.__typedelieu
    
    def get_topographie(self):
        return self.__topographie

    def get_population(self):
        return self.__population

    def get_position(self):
        return self.__position

    def get_proprietaire(self):
        return self.__proprietaire

#setter
    def set_typedelieu(self, lieu):
        self.__weapon = lieu

    def set_topographie(self,topographie):
        self.__topographie=topographie

    def set_population(self,population):
        self.__population=population

    def set_position(self,position):
        return self.__position=position

    def set_proprietaire(self,proprietaire):
        return self.__proprietaire=proprietaire

