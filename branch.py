import pygame

class Branch(pygame.sprite.Sprite):

    def __init__(self, branch_texture):
        pygame.sprite.Sprite.__init__(self)
        self.image = branch_texture
        self.rect = self.image.get_rect()
        self.rect.topleft = (-2000, -2000)