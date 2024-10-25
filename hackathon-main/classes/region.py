class Region():
    def __init__(self,typedelieu,topographie,population,position,proprietaire:str):
        #Population est un dictionnaire {creature: nombre_individus}
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
        self.__position=position

    def set_proprietaire(self,proprietaire):
        self.__proprietaire=proprietaire

    def compter_individus(self, creature):
        return self.__population.get(creature, 0)

    def ajouter_creature(self, creature, quantite=1):
        if creature in self.__population:
            self.__population[creature] += quantite
        else:
            self.__population[creature] = quantite
        print(f"{quantite} {creature}(s) ont été ajouté(s) à la population.")

    def retirer_creature(self, creature, quantite=1):
        if creature in self.__population:
            if self.__population[creature] > quantite:
                self.__population[creature] -= quantite
                print(f"{quantite} {creature}(s) ont été retiré(s) de la population.")
            elif self.__population[creature] <= quantite:
                del self.__population[creature]
                print(f"Tous les {creature}(s) ont été retiré(s) de la population.")
        else:
            print(f"Aucun {creature} dans la population.")
