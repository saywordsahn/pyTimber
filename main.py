import enum

import pygame

class Side(enum.Enum):
    LEFT = 0,
    RIGHT = 1,
    NONE = 2

pygame.init()

clock = pygame.time.Clock()
fps = 60
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
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

# score
text_color = pygame.color.Color('white')
score = 0
text = 'Score: ' + str(score)
score_txt_surface = font.render(text, True, text_color)

branch_texture = pygame.image.load('graphics/branch.png').convert_alpha()
branches = []
for i in range(6):
    branch = pygame.sprite.Sprite()
    branch.image = branch_texture
    branch.rect = branch.image.get_rect()
    branch.rect.topleft = (-2000, -2000)
    branches.append(branch)
branch_positions = [Side.NONE for i in range(6)]


game_over = False

while True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit(0)

    screen.blit(bg, (0, 0))
    screen.blit(score_txt_surface, (0, 0))
    treeGroup.draw(screen)
    player_group.draw(screen)

    # update time bar
    time_remaining -= dt / 1000

    if time_remaining <= 0:
        game_over = True

    time_bar_current_width = time_remaining * time_bar_start_width / time_limit
    pygame.draw.rect(screen, red, pygame.Rect(time_bar_left, time_bar_top, time_bar_current_width, time_bar_height))

    pygame.display.flip()
    dt = clock.tick(fps)



