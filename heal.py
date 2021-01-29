if self.health_point < 100 :
    if (self.objects['nourriture'] != 0) and (event.key = pg.K_n):
        self.health_points = min(self.health_points + 10, 100)
        self.objects['nourriture'] -= 1
    if (self.objects['potion magique'] != 0) and (event.key = pg.K_p):
        self.health_point = 100
        self.objects['potion magique'] -= 1