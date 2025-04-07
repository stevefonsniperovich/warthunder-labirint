from pygame import *
from random import randint
font.init()
mixer.init()

win_size = 1400, 900
main_win = display.set_mode((win_size))
display.set_caption("tank maze")
background = transform.scale(image.load("wt image background.jpeg"), win_size)

main_win.blit(background,(0,0))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_length, player_width):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_length, player_width))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        main_win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def move(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 850:
            self.rect.y += self.speed
        if keys_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 1350:
            self.rect.x += self.speed

class Enemy(GameSprite):
    direction = 'left'
    def update(self, x1, x2):
        if self.rect.x <= x1:
            self.direction = 'right'
        if self.rect.x >= x2:
            self.direction = 'left'

        if self.direction == 'right':
            self.rect.x += self.speed
        if self.direction == 'left':
            self.rect.x -= self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_length):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.length = wall_length
        self.image = Surface((self.width, self.length))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

main_sprite = Player('hero_tank.png', 50, 50, 1, 70, 50)
enemy1_sprite = Enemy('enemy_1.png', 850, 250, 1, 70, 50)
enemy2_sprite = Enemy('enemy_2.png', 300, 550, 4, 70, 50)
enemy3_sprite = Enemy('enemy_3.png', 1150, 700, 1, 70, 50)
final1 = GameSprite('final_1.png', 1150, 850, 0, 70, 70)
final2 = GameSprite('final_2.png', 1150, 850, 0, 70, 70)

wall_1 = Wall(75, 0, 0, 0, 150, 375, 10)
wall_2 = Wall(75, 0, 0, 475, 0, 10, 225)
wall_3 = Wall(75, 0, 0, 0, 400, 475, 10)
wall_4 = Wall(75, 0, 0, 475, 310, 10, 100)
wall_5 = Wall(75, 0, 0, 475, 310, 325, 10)
wall_6 = Wall(75, 0, 0, 800, 200, 300, 10)
wall_7 = Wall(75, 0, 0, 1100, 310, 300, 10)
wall_8 = Wall(75, 0, 0, 950, 310, 10, 200)
wall_9 = Wall(75, 0, 0, 500, 560, 900, 10)
wall_10 = Wall(75, 0, 0, randint(50, 950), randint(580, 850), randint(10, 100), randint(10, 100))
wall_11 = Wall(75, 0, 0, randint(50, 950), randint(580, 850), randint(10, 100), randint(10, 100))
wall_12 = Wall(75, 0, 0, randint(50, 950), randint(580, 850), randint(10, 100), randint(10, 100))
wall_13 = Wall(75, 0, 0, randint(50, 950), randint(580, 850), randint(10, 100), randint(10, 100))
wall_14 = Wall(75, 0, 0, randint(50, 950), randint(580, 850), randint(10, 100), randint(10, 100))


mixer.music.load('main.ogg')
mixer.music.play()

#mixer.music.load('knocked_out')
# knocked_out = mixer.Sound('knocked_out')
# mixer.music.load('win')
# win = mixer.Sound('win')

clock = time.Clock()
FPS = 60

game = True
finish = False
font = font.Font(None, 100)
win = font.render('Победа', True, (255, 215, 0))
lose = font.render('Поражение', True, (255, 10, 20))
walls = sprite.Group()
walls.add(wall_1, wall_2, wall_3, wall_4, wall_5, wall_6, wall_7, wall_8, wall_9, wall_10, wall_11, wall_12, wall_13, wall_14)
while game:
    events = event.get()
    for e in events:
        if e.type == QUIT:
            game = False
    if finish != True:
        main_win.blit(background, (0, 0))
        main_sprite.reset()
        main_sprite.move()
        enemy1_sprite.reset()
        enemy1_sprite.update(825, 950)
        enemy2_sprite.reset()
        enemy2_sprite.update(100, 400)
        enemy3_sprite.reset()
        enemy3_sprite.update(1100, 1200)
        final1.reset()
        walls.draw(main_win)
        if sprite.collide_rect(main_sprite, final1):
            #win.play()
            main_win.blit(win, (400, 300))
            final2.reset()
            finish = True
        if sprite.spritecollide(main_sprite, walls, False) or sprite.collide_rect(main_sprite, enemy1_sprite) or sprite.collide_rect(main_sprite, enemy2_sprite) or sprite.collide_rect(main_sprite, enemy3_sprite):
            #knocked_out.play()
            main_win.blit(lose, (400, 300))
            finish = True
        clock.tick(FPS)
        display.update()
