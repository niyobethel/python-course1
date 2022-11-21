class vehucule:
    def __init__(self, marque, couleur):
        self.marque = marque
        self.couleur = couleur
    def affichage(self):
        print(self.marque + " , " +self.couleur)
    def modification_couleur(self,n_col):
        self.couleur = n_col