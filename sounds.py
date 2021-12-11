import pygame
from pygame import mixer

class Sounds:

    def __init__(self, volume):
        pygame.mixer.pre_init(44100, -16, 2, 512)
        mixer.init()

        self.chop_fx = pygame.mixer.Sound('img/chop.wav')
        self.chop_fx.set_volume(volume)

        self.death_fx = pygame.mixer.Sound("img/death.wav")
        self.death_fx.set_volume(volume)

        self.out_of_time_fx = pygame.mixer.Sound("img/out_of_time.wav")
        self.out_of_time_fx.set_volume(volume)