public class Magie():
    def __init__(self,nom:str,description:str,degat,cout,type1:str):
        self.__nom=nom 
        self.__description=description 
        self.__degat=degat
        self.__cout=cout
        self.__type1=type1


 # Getter et Setter pour nom
    def get_nom(self):
        return self.__nom

    def set_nom(self, nom):
        self.__nom = nom

    # Getter et Setter pour description
    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    # Getter et Setter pour degat
    def get_degat(self):
        return self.__degat

    def set_degat(self, degat):
        self.__degat = degat

    # Getter et Setter pour cout
    def get_cout(self):
        return self.__cout

    def set_cout(self, cout):
        self.__cout = cout

    # Getter et Setter pour type1
    def get_type1(self):
        return self.__type1

    def set_type1(self, type1):
        self.__type1 = type1
