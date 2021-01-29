class Combat():

    def __init__(self, personnage, ennemi, tour):
        # Tour = 0 si c'est au tour du personnage et 1 sinon
        self.personnage = personnage
        self.ennemi = ennemi

    def tour_suivant(self, self.personnage, self.ennemi, self.tour):
        if tour:
            personnage.health_points = max(0,personnage.health_points - ennemi.strength)
            if personnage.health_points == 0:
                break
        else:
            ennemi.health_points = max(0,ennemi.health_points - personnage.strength)
            if ennemi.health_points == 0:
                ennemi.laisser_objet()