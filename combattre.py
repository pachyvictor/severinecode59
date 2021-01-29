def combat(personnage: Character, ennemi: Ennemi):
    """ Cette fonction simule un combat entre le personnage
    et un ennemi """

    combat = True

    while combatpersonnage.health_points != 0 or ennemi.health_points != 0:
        personnage.health_points = max(0,personnage.health_points - ennemi.strength)
        if personnage.health_points == 0:
            break

        ennemi.health_points = max(0,ennemi.health_points - personnage.strength)
        if ennemi.health_points == 0:
            ennemi.laisser_objet()
