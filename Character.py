from random import randint

max_bag = 20
objets = {'*' : ('or', 0),
          'j' : ('potion magique', 5),
          '!' : ('épée', 3),
          '(' : ('arc et flèches', 3),
          '&' : ('armure', 3),
          '£' : ('parchemins', 2),
          '¤' : ('anneau de pouvoir', 10),
          'µ' : ('nourriture', 2)}

magasin = {'potion magique' : 50, 'épée' :  

class Individu:

    def __init__(self, position, health_points, strength):
        self.position = position
        self.health_points = health_points
        self.strength = strength

    def blessure(self, coup):
        self.health_points = max(0, self.health_points - coup)

class Character(Individu):

    def __init__(self, objects, bag):
        Individu.__init__(self, position, health_points, strength)
        self.objects = objects
        self.bag = bag

    def recup_objet(self):
        point = carte(self.position)
        if point in objets:
            if objets[point][1] + self.bag <= max_bag:
                if objets[point][0] != 'or':
                    if want_to_recup(self):
                        self.objects[objets[point][0]] += 1
                        self.bag += objets[point][1]
                quantite_or = 5*randint(1, 5)
                self.objects['or'] += quantite_or

    def 

                
                
                







    