class Ennemi():

    def __init__(self, position, health_points, strength, object, taille_patrouille):
        self.position = position
        self.health_points = health_points
        self.strength = strength
        self.object = object
        self.etat = etat
        self.taille_patrouille = taille_patrouille

    def blessure(self, coup):
        self.health_points = max(0, self.health_points - coup)

    def avancer(self, position):
        etat = 0
        if etat == 0:
            for i in range(taille_patrouille):
                self.position[1] += 1
        elif etat == 1:
            for i in range(taille_patrouille):
                self.position[0] += 1
        elif etat == 2:
            for i in range(taille_patrouille):
                self.position[1] -= 1
        elif etat == 3:
            for i in range(taille_patrouille):
                self.position[0] -= 1

        if etat != -1:
            etat = (etat + 1)%4

    def laisser_objet(self):
        carte[position[0]][position[1]] = object