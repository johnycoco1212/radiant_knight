import pygame
from sources import tools,default
class Load :
    def __init__(self):
        self.state_name = 'load'
        self.finish = False
        self.next = 'cpt1'

        self.time = 0
        self.set_background()

    def set_background(self):
        self.image = tools.capture('./data/menu/load.png',0,0,800,611,(0,0,0),default.SCREEN_WIDTH,default.SCREEN_HEIGHT)
        pass

    def update(self,surface,keys):
        self.draw(surface)
        if self.time == 0:
            self.time = pygame.time.get_ticks()
        if pygame.time.get_ticks() - self.time > 2000:

            self.time = 0
            self.finish = True

    def draw(self,surface):
        surface.blit(self.image,(0,0))
