import pygame, colors, time
from random import randint

class player(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((40, 40))
        self.image.fill(colors.red)
        self.rect=self.image.get_rect()
        self.rect.x=WIDTH/2
        self.rect.y=HEIGHT-40
        self.score=0
class object(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 40))
        self.image.fill(colors.green)
        self.rect = self.image.get_rect()
        self.speed=0