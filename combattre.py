class Combat():

    def __init__(self, personnage, ennemi, tour, termine = False):
        # Tour = 0 si c'est au tour du personnage et 1 sinon
        self.personnage = personnage
        self.ennemi = ennemi
        self.tour = tour
        self.termine = termine

    def tour_suivant(self):
        if self.tour:
            personnage.health_points = max(0,personnage.health_points - ennemi.strength)
            if personnage.health_points == 0:
                if personnage.objects['potion magique'] != 0:
                    personnage.health_points = 50
                    personnage.objects['potion magique'] -= 1
                self.termine = True
                #faire GAME OVER
        else:
            ennemi.health_points = max(0,ennemi.health_points - personnage.strength)
            if ennemi.health_points == 0:
                ennemi.laisser_objet()
                personnage.health_points = min(100, 1.2 * personnage.health_points)
                personnage.strength += 0.1 * ennemi.strength
                self.termine = True
        tour = 1 - tour
