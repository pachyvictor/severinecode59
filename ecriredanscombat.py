if tableau[personnage.position[0] + 1][personnage.position[1]] == "§" \
or tableau[personnage.position[0] - 1][personnage.position[1]] == "§" \
or tableau[personnage.position[0]][personnage.position[1] + 1] == "§" \
or tableau[personnage.position[0]][personnage.position[1] - 1] == "§":
    for monstre in monstres:
        if monstre.position == [personnage.position[0] - 1, personnage.position[1]] or \
        monstre.position == [personnage.position[0] + 1, personnage.position[1]] or \
        monstre.position == [personnage.position[0], personnage.position[1] - 1] or \
        monstre.position == [personnage.position[0], personnage.position[1] + 1]:
        ennemi_actuel = monstre
    combatactuel = Combat(personnage, ennemi_actuel, 0, False)
    while not combat:
        clock.tick(10)
        
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_c:
                    combatactuel.tour_suivant()
