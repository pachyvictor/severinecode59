magasin = {pg.K_p : ('potion magique', 50), pg.K_e : ('épées', 10), pg.K_f : ('arcs et flèches', 20), pg.K_a : ('armure', 25), pg.K_v : ('parchemins', 5), pg.K_n : ('nourriture', 5)} 

#à mettre dans la deuxième boucle while

for event in pygame.event.get():
    touche = event.key
    if touche in magasin:
        if self.objects['or'] < magasin[touche][1]:
            return ("Vous ne pouvez pas acheter cet objet")
        self.objects[magasin[touche][0]] += 1
        self.objects['or'] -= magasin[touche][1]
