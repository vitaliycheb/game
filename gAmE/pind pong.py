from pygame import *

run = True
player_speed = 0
clock = time.Clock()
fps = 30

window = display.set_mode((700, 500))
display.set_caption("game")
bg = transform.scale(image.load("images/fon.jpg") , (700, 500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speedd, player_w, player_h):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_w, player_h))
        self.speed = player_speedd
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.width = player_w
        self.height = player_h
        global player_speed
        player_speed = player_speedd

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    

    def update(self):
        keys = key.get_pressed()

        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 355:
            self.rect.y += self.speed

player = Player("images/palka.png", -180, 210, 5, 400, 130)

class Ball(GameSprite):
    
    speed_x = player_speed
    speed_y = player_speed
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.x <= 0:
            self.rect.x = 1
            self.speed_x = self.speed_x*-1
        if self.rect.x >= 669:
            self.rect.x = 668
            self.speed_x = self.speed_x*-1
        if self.rect.y <= 0:
            self.rect.y = 1
            self.speed_y = self.speed_y*-1
        if self.rect.y >= 460:
            self.rect.y = 459
            self.speed_y = self.speed_y*-1
    

ball = Ball("images/ball.jpg", 350, 250, 2, 40, 40)

while run:
    for i in event.get():
        if i.type == QUIT:
            run = False
    


    window.blit(bg, (0, 0))

    player.reset()
    player.update()
    ball.reset()
    ball.update()

    display.update()
    clock.tick(fps)     