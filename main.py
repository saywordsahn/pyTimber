import enum
import random as rand
import pygame

from branch import Branch
from side import Side
from branches import Branches
pygame.init()

clock = pygame.time.Clock()
fps = 60
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
font = pygame.font.Font(None, 104)

# background
bg = pygame.image.load('graphics/background.png')

# colors
red = pygame.color.Color('red')

# tree
tree = pygame.sprite.Sprite()
tree.image = pygame.image.load('graphics/tree.png')
tree.rect = tree.image.get_rect()
tree.rect.topleft = (810, 0)
treeGroup = pygame.sprite.Group(tree)

# timer
time_bar_start_width = 400
time_bar_height = 80
time_bar_left = screen_width / 2 - time_bar_start_width / 2
time_bar_top = 980
time_limit = 6.0
time_remaining = 6.0
dt = 0.0

# player
player = pygame.sprite.Sprite()
player.image = pygame.image.load('graphics/player.png').convert_alpha()
player.rect = player.image.get_rect()
player.rect.topleft = (580, 720)
player.side = Side.LEFT
player_group = pygame.sprite.Group(player)

# axe
axe = pygame.sprite.Sprite()
axe.image = pygame.image.load('graphics/axe.png').convert_alpha()
axe.rect = axe.image.get_rect()
axe.rect.topleft = (700, 830)
# line the axe up with the tree
axe_position_left = 700
axe_position_right = 1075
player_group.add(axe)

# grave
grave = pygame.sprite.Sprite()
grave.image = pygame.image.load('graphics/rip.png').convert_alpha()
grave.rect = grave.image.get_rect()

# score
text_color = pygame.color.Color('white')
score = 0

branches = Branches()



game_over = False
accept_input = True

while True:

    for event in pygame.event.get():

        if event.type == pygame.KEYUP and not accept_input:
            accept_input = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit(0)

            if not game_over:
                if event.key == pygame.K_RIGHT and accept_input:
                    player.side = Side.RIGHT
                    score += 1

                    # add some time
                    time_remaining += (2 / score) + .15
                    axe.rect.topleft = (axe_position_right, axe.rect.y)
                    player.rect.topleft = (1200, 720)
                    branches.update()
                    accept_input = False


                if event.key == pygame.K_LEFT and accept_input:
                    player.side = Side.LEFT
                    score += 1

                    # add some time
                    time_remaining += (2 / score) + .15
                    axe.rect.topleft = (axe_position_left, axe.rect.y)
                    player.rect.topleft = (580, 720)
                    branches.update()
                    accept_input = False

    if branches.bottom_branch_position == player.side:
        print('branch pos:',branches.bottom_branch_position)
        print(player.side)
        grave.rect.topleft = player.rect.topleft
        player_group.remove(player)
        player_group.remove(axe)
        player_group.add(grave)
        text = 'YOU WERE CRUSHED!!! '
        game_over_text_surface = font.render(text, True, text_color)
        game_over = True

        # update time bar
    time_remaining -= dt / 1000

    if time_remaining <= 0:
        text = 'YOU RAN OUT OF TIME!!! '
        game_over_text_surface = font.render(text, True, text_color)
        game_over = True

    time_bar_current_width = time_remaining * time_bar_start_width / time_limit



    # draw to screen
    screen.blit(bg, (0, 0))
    text = 'Score: ' + str(score)
    score_txt_surface = font.render(text, True, text_color)
    screen.blit(score_txt_surface, (0, 0))
    treeGroup.draw(screen)
    branches.draw(screen)
    player_group.draw(screen)
    pygame.draw.rect(screen, red, pygame.Rect(time_bar_left, time_bar_top, time_bar_current_width, time_bar_height))

    if game_over:
        screen.blit(game_over_text_surface, (600, 500))





    pygame.display.flip()
    dt = clock.tick(fps)



