from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_0(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
    
        if keys_pressed[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

    def update_1(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
    
        if keys_pressed[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

win_width = 700
win_height = 500
back = (255, 194, 151)

window = display.set_mode((win_width, win_height))
display.set_caption('Ping-Pong')
background = transform.scale(image.load('pong.png'), (win_width, win_height))

racket_0 = Player('racket.png', 0, 10, 65, 65, 4)

racket_1 = Player('racket.png', 0, 15, 65, 65, 4)



game = True
finish = False

clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background, (0, 0))

        racket_0.update_0()
        racket_1.update_1()

        racket_0.reset()
        racket_1.reset()
    
    display.update()
    clock.tick(FPS)








































































































































































# from pygame import *
# from random import randint
# from time import time as timer

# mixer.init()
# mixer.music.load("space.ogg")
# mixer.music.play()
# bullet_sound = mixer.Sound("fire.ogg")

# lost = 0
# score = 0
# life = 3
# asteroid_y = 620

# font.init()
# font1 = font.Font(None, 36)

# font2 = font.Font(None, 36)

# class GameSprite(sprite.Sprite):
#     def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
#         super().__init__()
#         self.image = transform.scale(image.load(player_image), (size_x, size_y))
#         self.speed = player_speed
#         self.rect = self.image.get_rect()
#         self.rect.x = player_x
#         self.rect.y = player_y
    
#     def reset(self):
#         window.blit(self.image, (self.rect.x, self.rect.y))

# class Player(GameSprite):
#     def update(self):
#         keys_pressed = key.get_pressed()

#         if keys_pressed[K_a] and self.rect.x > 5:
#             self.rect.x -= self.speed
    
#         if keys_pressed[K_d] and self.rect.x < win_width - 80:
#             self.rect.x += self.speed

#     def fire(self):
#         bullet = Bullet("bullet.png", self.rect.centerx, self.rect.top, 15, 20, 15)
#         bullets.add(bullet)

# class Enemy(GameSprite):
#     def update(self):
#         self.rect.y += self.speed
#         global lost
#         if self.rect.y > 500:
#             self.rect.y = 0
#             self.rect.x = randint(80, 620)
#             lost += 1

# class Asteroid(GameSprite):
#     def update(self):
#         self.rect.y += self.speed
#         global lost
#         if self.rect.y > 500:
#             self.rect.y = 0
#             self.rect.x = randint(80, 620)
#             lost += 1

# class Bullet(GameSprite):
#     def update(self):
#         self.rect.y -= self.speed
#         if self.rect.y < 0:
#             self.kill()

# win_width = 700
# win_height = 500

# ship = Player('rocket.png', 5, win_height - 80, 65, 65, 4)

# enemies = sprite.Group()
# for i in range(1,6):
#     enemy = Enemy('ufo.png', randint(80, 620), 5, 55, 55, 2)
#     enemies.add(enemy)

# bullets = sprite.Group()

# asteroids = sprite.Group()
# for a in range(1,3):
#     asteroid = Asteroid('asteroid.png', randint(80, asteroid_y), 5, 55, 55, randint(1,2))
#     asteroids.add(asteroid)

# window = display.set_mode((win_width, win_height))
# display.set_caption('Shoter_game')
# background = transform.scale(image.load('galaxy.jpg'), (win_width, win_height))

# game = True
# finish = False

# clock = time.Clock()
# FPS = 60
# text_lose = font1.render(
#     "Пропущенно" + str(lost), 1, (255, 255, 255)
# )

# while game:
#     for e in event.get():
#         if e.type == QUIT:
#             game = False
#         elif e.type == KEYDOWN:
#             if e.key == K_SPACE:
#                 bullet_sound.play()
#                 ship.fire()

#     if not finish:
#         window.blit(background, (0, 0))

#         text = font2.render("Счет" + str(score), 1, (255, 255, 255))
#         window.blit(text, (10, 20))

#         text_lose = font2.render("Пропущенно" + str(lost), 1, (255, 255, 255))
#         window.blit(text_lose, (10, 50))


#         ship.update()
#         enemies.update()
#         asteroids.update()
#         bullets.update()

#         ship.reset()
#         enemies.draw(window)
#         asteroids.draw(window)
#         bullets.draw(window)

#         collides = sprite.groupcollide(enemies, bullets, True, True)
#         for c in collides:
#             score = score + 1
#             enemy = Enemy('ufo.png', randint(80, 620), 5, 40, 80, 2)
#             enemies.add(enemy)

#         collides = sprite.groupcollide(asteroids, bullets, False, True)
#         for c in collides:
#             asteroid = Asteroid('asteroid.png', randint(80, 620), 5, 55, 55, randint(1,2))

#         if sprite.spritecollide(ship, enemies, True) or sprite.spritecollide(ship, asteroids, True):
#             life = life - 1
            
#         if asteroid_y > 620:
#             asteroids.add(asteroid)

#         if life == 0 or lost >= 10:
#             finish = True
#             # window.blit(lose, (200, 200))

#         if score == 10:
#             finish = True
#             # window.blit(win, (200, 200))

#         if life == 3:
#             life_color = (0, 150, 0)
        
#         if life == 2:
#             life_color = (150, 150, 0)

#         if life == 1:
#             life_color = (150, 0, 0)

#         text_life = font1.render(str(life), 1, life_color)
#         window.blit(text_life, (650, 10))

#     else:
#         finish = False
#         lost = 0
#         score = 0
#         life = 3
#         for b in bullets:
#             b.kill()
#         for i in enemies:
#             i.kill()
        
#         time.delay(3000)
#         for m in range(1, 6):
#             enemy = Enemy('ufo.png', randint(80, 620), 5, 55, 55, 2)
#             enemies.add(enemy)

#         for a in range(1,3):
#             asteroid = Asteroid('asteroid.png', randint(80, 620), 5, 55, 55, randint(1,2))
#             enemies.add(asteroid)

#     display.update()
#     clock.tick(FPS)