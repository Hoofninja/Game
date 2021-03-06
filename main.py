import os
import pygame


# Asset folders
game_folder = os.path.dirname(__file__)
maps_folder = os.path.join(game_folder, 'maps')


# Map
# Read .txt file from 'maps', convert data to variable.
map_1 = os.path.join(maps_folder, 'test_map_1.txt')
map_file = open(map_1, 'r')
lines = map_file.readlines()
x_map = []
xy_map = []
hits = []

for element in lines:
    x_map = []
    for i in element:
        if i not in [' ', '\n']:
            x_map.append(i)
    xy_map.append(x_map)


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)


# Walls sprites
class Wall(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.Surface((30, 30))
        self.image.fill(GRAY)
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.speed = 0


# Player sprite
class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (len(xy_map[0])*30/2, len(xy_map)*30/2)
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        self.speed_x = 0
        self.speed_y = 0
        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_LEFT]:
            self.rect.x += -1
            if len(pygame.sprite.spritecollide(player, walls, False)) != 0:
                self.rect.left += 1
        if key_state[pygame.K_RIGHT]:
            self.rect.x += 1
            if len(pygame.sprite.spritecollide(player, walls, False)) != 0:
                self.rect.right += -1
        if key_state[pygame.K_UP]:
            self.rect.y += -1
            if len(pygame.sprite.spritecollide(player, walls, False)) != 0:
                self.rect.top += 1
        if key_state[pygame.K_DOWN]:
            self.rect.y += 1
            if len(pygame.sprite.spritecollide(player, walls, False)) != 0:
                self.rect.bottom += -1


# Create game window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((len(xy_map[0])*30, len(xy_map)*30))
pygame.display.set_caption('My Game')
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
walls = pygame.sprite.Group()

# Wall creation
for i in range(len(xy_map)):
    for j in range(len(xy_map[i])):
        if xy_map[i][j] == 'x':
            wall = Wall(j*30, i*30)
            all_sprites.add(wall)
            walls.add(wall)

# Player creation
player = Player()
all_sprites.add(player)

# Game cycle
FPS = 240
running = True
while running:
    # Iterations per second
    clock.tick(FPS)
    # Event input
    for event in pygame.event.get():
        # quit condition
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    # Render
    screen.fill(GREEN)
    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()
