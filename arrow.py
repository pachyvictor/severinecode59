if event.key == pg.K_y:
    personnage.arc_bande = 1 - personnage.arc_bande

if personnage.arc_bande and event.key == pg.K_z and personnage.objects["arcs et flèches"] > 0:
    fleche_tiree = (True, "haut")
    personnage.objects["arcs et flèches"] -= 1
    personnage.pos_fleche = [personnage.position[0] - 1, personnage.position[1]]

elif personnage.arc_bande and event.key == pg.K_q and personnage.objects["arcs et flèches"] > 0:
    fleche_tiree = (True, "gauche")
    personnage.objects["arcs et flèches"] -= 1
    personnage.pos_fleche = [personnage.position[0], personnage.position[1] - 1]

elif personnage.arc_bande and event.key == pg.K_d and personnage.objects["arcs et flèches"] > 0:
    fleche_tiree = (True, "droite")
    personnage.objects["arcs et flèches"] -= 1
    personnage.pos_fleche = [personnage.position[0], personnage.position[1] + 1]

elif personnage.arc_bande and event.key == pg.K_s and personnage.objects["arcs et flèches"] > 0:
    fleche_tiree = (True, "bas")
    personnage.objects["arcs et flèches"] -= 1
    personnage.pos_fleche = [personnage.position[0] + 1, personnage.position[1]]

if fleche_tiree[0]:
    if fleche_tiree[1] == "haut":
        personnage.pos_fleche = [personnage.position[0] - 1, personnage.position[1]]
        if tableau[personnage.pos_fleche[0]][personnage.pos_fleche[1]] == "§":
            for monstre in monstres:
                if [personnage.pos_fleche[0], personnage.pos_fleche[1]] == monstre.position:
                    monstre.blessure()
        personnage.pos_fleche = None

    elif fleche_tiree[1] == "bas":
        personnage.pos_fleche = [personnage.position[0] + 1, personnage.position[1]]
        if tableau[personnage.pos_fleche[0]][personnage.pos_fleche[1]] == "§":
            for monstre in monstres:
                if [personnage.pos_fleche[0], personnage.pos_fleche[1]] == monstre.position:
                    monstre.blessure()
        personnage.pos_fleche = None

    elif fleche_tiree[1] == "droite":
        personnage.pos_fleche = [personnage.position[0], personnage.position[1] + 1]
        if tableau[personnage.pos_fleche[0]][personnage.pos_fleche[1]] == "§":
            for monstre in monstres:
                if [personnage.pos_fleche[0], personnage.pos_fleche[1]] == monstre.position:
                    monstre.blessure()
        personnage.pos_fleche = None

    elif fleche_tiree[1] == "gauche":
        personnage.pos_fleche = [personnage.position[0], personnage.position[1] - 1]
        if tableau[personnage.pos_fleche[0]][personnage.pos_fleche[1]] == "§":
            for monstre in monstres:
                if [personnage.pos_fleche[0], personnage.pos_fleche[1]] == monstre.position:
                    monstre.blessure()
        personnage.pos_fleche = None

    if tableau[personnage.pos_fleche[0]][personnage.pos_fleche[1]] in ["_", "|"]:
        personnage.pos_fleche = None
