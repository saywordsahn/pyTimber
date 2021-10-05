import pygame
import random as rand
from branch import Branch
from side import Side


class Branches(pygame.sprite.Group):

    def __init__(self):
        pygame.sprite.Group.__init__(self)
        self.branch_texture = pygame.image.load('graphics/branch.png').convert_alpha()
        self.bottom_branch_position = Side.NONE

    def update(self):

        self.bottom_branch_position = Side.NONE

        for branch in self.sprites():
            branch.update()

            if branch.pos >= 5:
                self.bottom_branch_position = branch.side
                branch.kill()

        # spawn new branch at pos 0
        rand.seed()
        randomNum = rand.randint(0, 4)
        if randomNum == 0:
            self.add(Branch(self.branch_texture, Side.LEFT))
        elif randomNum == 1:
            self.add(Branch(self.branch_texture, Side.RIGHT))

