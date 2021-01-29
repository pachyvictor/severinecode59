class Ennemi(Individu):

    def __init__(self, object, etat):
        Individu.__init__(self,position, health_points, strength)
        self.left_object = left_object
        self.etat = etat

    def avancer(self, position):
        if etat == 0:
            self.position[1] += 1
        elif etat == 1:
            self.position[0] += 1
        elif etat == 2:
            self.position[1] -= 1
        elif etat == 3:
            self.position[0] -= 1

        if etat != -1:
            etat = (etat + 1)%4

    def laisser_objet(self):
        carte[position[0]][position[1]] = object