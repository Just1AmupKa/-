#Создай собственный Шутер!

from pygame import *
from random import randint

display.set_caption("Shooter")
window = display.set_mode((1440, 720))
background = transform.scale(image.load('galaxy.jpg'), (1440, 720))

# СДЕЛАТЬ
# кол-во врагов увеличивалось
# создать бонус для стрельбы бешенной
# создать дубликат корабля как бонус
# сердечки интерфейса жизней
# дружеские кораблики по которым нельзя стрелять
# босс лвл сделать





lost = 0 # количество пропущенных врагов######################################3
score = 0 # счетчик убитых

#фоновая музыка
mixer.init()
mixer.music.load('f7c571af32330a5(1).mp3')
mixer.music.play()

class GameSprite(sprite.Sprite):
    def init(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.init(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        # самостоятельно
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x >5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x <1360:
            self.rect.x += self.speed


    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, 10)
        bullets.add(bullet)

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost 
        if self.rect.y >= 800:
            lost += 1 
            self.rect.y = randint(-500, -50)
            self.rect.x = randint(100, 1200)

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

ship = Player('rocket.png', 5, 600, 60, 80, 20)

monsters = sprite.Group()
bullets = sprite.Group()

for i in range(7):
    monster = Enemy("ufo.png", randint(100, 1200), randint(-600, -100), 128, 65, 5)
    monsters.add(monster)

finish = False
game = True
clock = time.Clock()

fire_sound = mixer.Sound('fire.ogg')
font.init()
fint_universal = font.Font(None, 36)

# также необходимо создать поле текста отвечающее за убитых врагов
# текст который необходимо выводить "Врагов убито:" + переменная score
# отобразить данное поле текста под полем с количеством пропущенных врагов

strelyat_on = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                strelyat_on = True
        elif e.type == KEYUP:
            if e.key == K_SPACE:
                strelyat_on = False

                                            # сделать так, чтобы когда вы зажимаете пробел пули лети постоянно


    if strelyat_on:
        ship.fire()
        

    window.blit(background,(0,0))

    text_lost_enemys = fint_universal.render('Пропущено: ' + str(lost), 1, (255,255,255))
    test_score_enemys = fint_universal.render('Врагов убито: ' + str(score), 1, (255,255,255))


    

    
    if not finish: # пока идет игра
        ship.reset()
        ship.update()

        
        monsters.draw(window)
        monsters.update()

        bullets.draw(window)
        bullets.update()

        window.blit(text_lost_enemys, (10,10))
        window.blit(test_score_enemys, (10,50))


        display.update()
    clock.tick(60)
