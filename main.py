import enum
import random as rand
import pygame

class Side(enum.Enum):
    LEFT = 0,
    RIGHT = 1,
    NONE = 2

def update_branches():
    global branch_positions

    # move all the branchs down one spot in the list (0 is top, 5 is bottom)
    for i in range(5, 0, -1):
        branch_positions[i] = branch_positions[i - 1]

    # spawn new branch at pos 0
    rand.seed()
    randomNum = rand.randint(0, 4)
    if randomNum == 0:
        branch_positions[0] = Side.LEFT
    elif randomNum == 1:
        branch_positions[0] = Side.RIGHT
    else:
        branch_positions[0] = Side.NONE


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


# branches
branch_texture = pygame.image.load('graphics/branch.png').convert_alpha()
branches = []
num_branches = 6
for i in range(num_branches):
    branch = pygame.sprite.Sprite()
    branch.image = branch_texture
    branch.rect = branch.image.get_rect()
    branch.rect.topleft = (-2000, -2000)
    branches.append(branch)
branch_positions = [Side.NONE for i in range(6)]


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

            if event.key == pygame.K_RIGHT and accept_input:
                player.side = Side.RIGHT
                score += 1

                # add some time
                time_remaining += (2 / score) + .15
                axe.rect.topleft = (axe_position_right, axe.rect.y)
                player.rect.topleft = (1200, 720)
                update_branches()
                accept_input = False


            if event.key == pygame.K_LEFT and accept_input:
                player.side = Side.LEFT
                score += 1

                # add some time
                time_remaining += (2 / score) + .15
                axe.rect.topleft = (axe_position_left, axe.rect.y)
                player.rect.topleft = (580, 720)
                update_branches()
                accept_input = False

    screen.blit(bg, (0, 0))
    text = 'Score: ' + str(score)
    score_txt_surface = font.render(text, True, text_color)
    screen.blit(score_txt_surface, (0, 0))
    treeGroup.draw(screen)
    player_group.draw(screen)

    # for i in range(num_branches):
    #     height = i * 150
    #     if branch_positions[i] == Side.LEFT:
    #         # move the sprite to the left side
    #         branches[i].rect.topleft = (610, height)


    # update time bar
    time_remaining -= dt / 1000

    if time_remaining <= 0:
        game_over = True

    time_bar_current_width = time_remaining * time_bar_start_width / time_limit
    pygame.draw.rect(screen, red, pygame.Rect(time_bar_left, time_bar_top, time_bar_current_width, time_bar_height))

    pygame.display.flip()
    dt = clock.tick(fps)



