import pygame
class Enemy(object):
    def __init__(self,x,y):
        self.rect=pygame.Rect(x,y,58,56)
    def move(self,xmove,ymove):
        self.rect.x=self.rect.x+xmove
        self.rect.y=self.rect.y+ymove
    def draw(self):
        window.blit(enemyimg, self.rect)
class Player(object):
    def __init__(self,yaxis):
        self.x=0
        self.y=636
        self.yaxis=yaxis
        self.rect=pygame.Rect(self.x,self.y,29,28)
    def yaxisenb(self,yaxis):
        if yaxis == "1":
            self.yaxis=True
        else:
            self.yaxis=False
    def move(self,x,y):
        self.rect.x=x-43
        if self.yaxis == True:
            self.rect.y=y
    def draw(self):
        window.blit(playerimg, self.rect)
    def checkcoll(self,rect1):
        return self.rect.colliderect(rect1)
class Bullet(object):
    def __init__(self,skin,x,y):
        self.x=x
        self.y=y
        self.skin=skin
        self.rect=pygame.Rect(x,y,9,28)
    def move(self,xmove,ymove):
        self.rect.x=self.rect.x+xmove
        self.rect.y=self.rect.y+ymove
    def draw(self):
        window.blit(self.skin,self.rect)
    def teleport(self,x,y):
        self.rect.x=x
        self.rect.y=y
    def checkcoll(self,rect1):
        return self.rect.colliderect(rect1)
enemyimg=pygame.image.load("enemy.png")
playerimg=pygame.image.load("player.png")
playerimg=pygame.transform.scale(playerimg, (87,84))
enemyimg=pygame.transform.scale(enemyimg, (58,56))
bullet1=pygame.image.load("bullet.png")

window=pygame.display.set_mode((720, 720))
#window=pygame.display.set_mode((720,720), pygame.FULLSCREEN)
running=True
player=Player(False)
enemy=Enemy(0,0)
bullet=Bullet(bullet1,100,100)
#player.yaxisenb("1")
while running:
    pygame.draw.rect(window, (0,0,0),(0,0,1280,1280))

    if bullet.checkcoll(enemy):
        print "Collsion"
    bullet.move(0,-1)
    bullet.draw()
    x,y=pygame.mouse.get_pos()
    player.move(x,y)
    player.draw()
    enemy.draw()
    #enemy.move(1,0)
    if pygame.mouse.get_pressed()[0] and bullet.rect.y < -27:
        bullet.teleport(player.rect.x+39, player.rect.y)
    keys=pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running=False
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
pygame.display.quit()
pygame.quit()
