from pygame import *


class GameSprite(sprite.Sprite):    #parent class
    def __init__(self, player_image, player_x, player_y, size_x, size_y, number):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.number = number
    def reseted(self):
        window.blit(self.image, (self.rect.x, self.rect.y))         #drawing an object

class Player(GameSprite):     #class for player creations
    def __init__(self, player_image, player_x, player_y, size_x, size_y, number, player_speed):
        super().__init__(player_image, player_x, player_y, size_x, size_y, number)
        self.player_speed = player_speed
    def move(self):
        keys_pressed = key.get_pressed()
        if self.number == 1:                          #movement of the first player
            if keys_pressed[K_w] and self.rect.y > 2:
                self.rect.y -= 3.5
            if keys_pressed[K_s] and self.rect.y < 420:
                self.rect.y += 3.5

        if self.number == 2:                        #movement of the second player
            if keys_pressed[K_UP] and self.rect.y > 2:
                self.rect.y -= 3.5
            if keys_pressed[K_DOWN] and self.rect.y < 420:
                self.rect.y += 3.5
class Enemy(GameSprite): # class for ball
    def __init__(self, player_image, player_x, player_y, size_x, size_y, number, speed_x, speed_y):
        super().__init__(player_image, player_x, player_y, size_x, size_y, number)
        self.speed_x = speed_x
        self.speed_y = speed_y
    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y > win_height - 50 or self.rect.y < 0:
            self.speed_y *= -1

win_height = 500
win_width = 700

window = display.set_mode((win_width, win_height))
display.set_caption('Ping-Pong')
background = transform.scale(image.load('playground.jpg'), (700, 500))
run = True

player1 = Player('platform.png', 25, 205, 30, 100, 1, 3)
player2 = Player('platform.png', 650, 205, 30, 100, 2, 3)
ball = Enemy('ball.png', 327, 230, 50, 50, 3, 2, 2)

font.init()
font = font.Font(None, 55)
lose1 = font.render('PLAYER 1 LOSE!', True, (250, 78, 5))
lose2 = font.render('PLAYER 2 LOSE!', True, (250, 78, 5))

fps = 60
finish = False
clock = time.Clock()
while run:
    if finish != True:
        window.blit(background, (0, 0))
        player1.reseted()
        player2.reseted()
        ball.reseted()

        player1.move()
        player2.move()
        ball.move()
        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            ball.speed_x *= -1
            ball.speed_y *= 1

        if ball.rect.x < 0:  #the loss of the first player
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.x > win_width:  #the loss of the second player
            finish = True
            window.blit(lose2, (200, 200))

    for e in event.get():
        if e.type == QUIT:
            run = False

    clock.tick(fps)
    display.update()
