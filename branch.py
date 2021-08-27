import pygame
from side import Side

class Branch(pygame.sprite.Sprite):

    def __init__(self, branch_texture, side):
        pygame.sprite.Sprite.__init__(self)
        self.image = branch_texture
        self.rect = self.image.get_rect()
        self.rect.topleft = (-2000, -2000)
        self.side = side
        self.pos = 0
        self.rect.y = 0
        if side == Side.LEFT:
            self.rect.x = 410
            self.image = pygame.transform.flip(self.image, True, False)
        else:
            self.rect.x = 1060

    def update(self):
        self.pos += 1
        self.rect.y = self.pos * 150