from random import randint
import pygame
from pygame.locals import *

max_bag = 20
objets = {'*' : ('or', 0),
          'j' : ('potion magique', 5),
          '!' : ('épées', 3),
          '(' : ('arcs et flèches', 3),
          '&' : ('armure', 3),
          '£' : ('parchemins', 2),
          '¤' : ('anneau de pouvoir', 10),
          'µ' : ('nourriture', 2)}

magasin = {pg.K_p : ('potion magique', 50), pg.K_e : ('épées', 10), pg.K_f : ('arcs et flèches', 20), pg.K_a : ('armure', 25), pg.K_v : ('parchemins', 5), pg.K_n : ('nourriture', 5)} 

objects_0 = {'or' : 0, 'potion magique' : 0, 'épées' : 0, 'arcs et flèches' : 0, 'armure' : 0, 'parchemins' : 0, 'anneau de pouvoir' : 0, 'nourriture' : 0}

class Character:

    def __init__(self, position = [1, 1], health_points = 100, strength = 15, objects = objects_0, bag = 0, arc_bande = 0, pos_fleche = None):
        self.position = position
        self.health_points = health_points
        self.strength = strength
        self.objects = objects
        self.bag = bag
        def.arc_bande = arc_bande
        def.pos_fleche = pos_fleche

    def blessure(self, coup):
        self.health_points = max(0, self.health_points - coup)

    def want_to_recup(self):


    def recup_object(self):
        point = carte(self.position)
        if point in objets:
            if objets[point][1] + self.bag <= max_bag:
                if objets[point][0] != 'or':
                    if want_to_recup(self):
                        self.objects[objets[point][0]] += 1
                        self.bag += objets[point][1]
                quantite_or = 5*randint(1, 5)
                self.objects['or'] += quantite_or

    def buy_object(self):
        for event in pygame.event.get():
            if event.type == pg.KEYDOWN:
                if self.objects['or'] != 0:
                    if event.key == pg.K_m:
                        event.key = touche
                        if touche in magasin:
                            if (self.objects['or'] >= magasin[touche][1]) and ()



    def heal(self):
        for event in pygame.event.get():
            if event.type == pg.KEYDOWN:
                if self.health_point < 100 :
                    if (self.objects['nourriture'] != 0) and (event.key = pg.K_n):
                        self.health_points = min(self.health_points += 10, 100)
                        self.objects['nourriture'] -= 1
                    if (self.objects['potion magique'] != 0) and (event.key = pg.K_p):
                        self.health_point = 100
                        self.objects['potion magique'] -= 1



                
                
                







    