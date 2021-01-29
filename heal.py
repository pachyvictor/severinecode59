import pygame as pg

clock = pygame.time.Clock()
pg.init()

continuer = True 
while continuer:
    
    for event in pygame.event.get() :
        if event.type == pg.KEYDOWN :
            if event.key = pg.K_h :
                if self.health_point < 100 :
                    if 'nourriture' in sac and event.key = pg.K_n :
                        self.health_point = min(self.health_position += 10 , 100)
                    if 'potion' in sac and event.key = pg.K_p :
                        self.health_point = 100