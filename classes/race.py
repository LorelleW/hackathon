class Race():
    def __init__(self,nom:str,region,rarete,reputation):
        self.__nom=nom 
        self.__region=region 
        self.__rarete=rarete #S ou A ou B ou C ou D avec S>A>B>C>D
        self.__reputation=reputation #?
#getter
    def get_nom(self):
        return self.__nom
    
    def get_region(self):
        return self.__region

    def get_rarete(self):
        return self.__rarete

    def get_reputation(self):
        return self.__reputation

#setter
    def set_nom(self, nom):
        self.__nom = nom

    def set_region(self, region):
        self.__region = region

    def set_rarete(self, rarete):
        self.__rarete = rarete

    def set_reputation(self, reputation):
        self.__reputation = reputation
