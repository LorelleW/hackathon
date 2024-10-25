class Inventaire():
    def __init__(self,livres,armures,armes,objets): #mettre un système % de chance
        #Les attributs de la classe sont des listes  
        self.__livres=livres
        self.__armures=armures
        self.__armes=armes
        self.__objets=objets

    def get_livres(self):
        return self.__livres

    def set_livres(self, livres):
        self.__livres = livres

    def get_armures(self):
        return self.__armures

    def set_armures(self, armures):
        self.__armures = armures

    def get_armes(self):
        return self.__armes

    def set_armes(self, armes):
        self.__armes = armes

    def get_objets(self):
        return self.__objets

    def set_objets(self, objets):
        self.__objets = objets

    def ajouter_livre(self, livre, quantite=1):
        for _ in range(quantite):
            self.__livres.append(livre)
        #print(f"{quantite} livre(s) '{livre}' ont été ajouté(s) à l'inventaire.")

    def retirer_livre(self, livre, quantite=1):
        count = 0
        while livre in self.__livres and count < quantite:
            self.__livres.remove(livre)
            count += 1
        #if count > 0:
            #print(f"{count} livre(s) '{livre}' ont été retiré(s) de l'inventaire.")
        #else:
            #print(f"Aucun livre '{livre}' n'a été trouvé dans l'inventaire.")
            
    def ajouter_armure(self, armure, quantite=1):
        for _ in range(quantite):
            self.__armures.append(armure)
        #print(f"{quantite} armure(s) '{armure}' ont été ajoutée(s) à l'inventaire.")

    def retirer_armure(self, armure, quantite=1):
        count = 0
        while armure in self.__armures and count < quantite:
            self.__armures.remove(armure)
            count += 1
        #if count > 0:
            #print(f"{count} armure(s) '{armure}' ont été retirée(s) de l'inventaire.")
        #else:
            #print(f"Aucune armure '{armure}' n'a été trouvée dans l'inventaire.")

    def ajouter_arme(self, arme, quantite=1):
        for _ in range(quantite):
            self.__armes.append(arme)
        #print(f"{quantite} arme(s) '{arme}' ont été ajoutée(s) à l'inventaire.")

    def retirer_arme(self, arme, quantite=1):
        count = 0
        while arme in self.__armes and count < quantite:
            self.__armes.remove(arme)
            count += 1
        #if count > 0:
            #print(f"{count} arme(s) '{arme}' ont été retirée(s) de l'inventaire.")
        #else:
            #print(f"Aucune arme '{arme}' n'a été trouvée dans l'inventaire.")

    def ajouter_objet(self, objet, quantite=1):
        for _ in range(quantite):
            self.__objets.append(objet)
        #print(f"{quantite} objet(s) '{objet}' ont été ajouté(s) à l'inventaire.")

    def retirer_objet(self, objet, quantite=1):
        count = 0
        while objet in self.__objets and count < quantite:
            self.__objets.remove(objet)
            count += 1
        #if count > 0:
            #print(f"{count} objet(s) '{objet}' ont été retiré(s) de l'inventaire.")
        #else:
            #print(f"Aucun objet '{objet}' n'a été trouvé dans l'inventaire.")

    def arme_in(self, arme):
        armes = Inventaire.get_armes(self)
        for a in armes:
            if (a == arme):
                return True
        return False

    def livre_in(self, livre):
        livres = Inventaire.get_livres(self)
        for a in livres:
            if (a == livre):
                return True
        return False

    def armure_in(self, armure):
        armures = Inventaire.get_armures(self)
        for a in armures:
            if (a == armure):
                return True
        return False


    def objet_in(self, objet):
        objets = Inventaire.get_objets(self)
        for a in objet:
            if (a == objet):
                return True
        return False








