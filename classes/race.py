public class Race():
    def __init__(self,nom:str,region:str,rarete,reputation):
        self.__nom=nom 
        self.__region=region 
        self.__rarete=rarete #int? str?
        self.__reputation=reputation #?

    def get_nom_race(self):
        return self.__nom
    
    def get_region_race(self):
        return self.__region

    def get_rarete_race(self):
        return self.__rarete

    def get_position_race(self):
        return self.__position

    def get_reputation_race(self):
        return self.__reputation
