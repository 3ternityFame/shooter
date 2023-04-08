#Создай собственный Шутер!
from pygame import *
from random import * 

window = display.set_mode((700, 500) )
display.set_caption("Бархатные тяги")
background = transform.scale(image.load('galaxy.jpg'), (700, 500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def upravlenie(self):
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= self.speed
        if keys[K_RIGHT]:
            self.rect.x += self.speed

    def update(self):
      self.rect.y += self.speed
      if self.rect.y > 640:
          self.rect.x = randint(40, 500)
          self.rect.y = 0
    def fire(self):
        bullet = Bullet("bullet.png", self.rect.centerx - 10, self.rect.x, -15)
        bullets.add(bullet)
    
class Bullet(GameSprite):
    def update(self):
        if self.rect.y < 5:
            self.kill()

bullets = sprite.Group()



player = GameSprite('rocket.png', 5, 420, 10)
monsters = sprite.Group()
for i in range(5):
    monster = GameSprite("ufo.png", randint(80, 620), -40, randint(1, 5))
    monsters.add(monster)


font.init()
font1 = font.Font(None, 36)


clock = time.Clock()
FPS = 60

clock.tick(FPS)

Lost = 0


finish = False

game = True
while game:
    window.blit(background, (0, 0))
    player.reset()
    monster.reset()
    monsters.draw(window)
    monsters.update()
    player.upravlenie()
    bullets.draw(window)
    bullets.update()
    kp = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            game = False
        if kp[K_SPACE]:
            player.fire()
    if sprite.groupcollide(monsters, bullets, True, True):
        score = score + 1
        monster = GameSprite("ufo.png", randint(80, 620), -40, 80, 50, randint(1, 5))
        monsters.add(monster)
        


    clock.tick(FPS)

    display.update()





