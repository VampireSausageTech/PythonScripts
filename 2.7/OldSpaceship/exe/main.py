import pygame, time
playerimg=pygame.image.load("Player.png")
enemyimg=pygame.image.load("enemy.png")
bulletimg=pygame.image.load("Bullet.png")
window = pygame.display.set_mode((640,640))
running=True
frames=0
def changex(xmve):
    global rows
    for i in rows:
        i.xmove=xmve
        i.rowy=i.rowy+20
def createrows():
    global rows
    rows=[]
    num=0
    while num < 5:
        rows.insert(num, Row())
        rows[num].changey(60*num)
        num=num+1
class Player(object):
    def __init__(self):
        self.rect = pygame.Rect(64,64,64,47)
    def teleport(self,x1,y1):
        self.rect.x=x1
        self.rect.y=y1
    def coord(self):
        return (self.rect.x,self.rect.y)
    def draw(self):
        window.blit(playerimg,(self.rect.x,self.rect.y))
class Enemy(object):
    x=64
    y=64
    def __init__(self):
        self.rect = pygame.Rect(64,64,64,47)
    def teleport(self,x1,y1):
        self.rect.x=x1
        self.rect.y=y1
        self.x=x1
        self.y=y1
    def move(self):
        self.rect.x=self.x
        self.rect.y=self.y
        #self.rect.y+=1
    def coord(self):
        return (self.rect.x,self.rect.y)
    def draw(self):
        window.blit(enemyimg,(self.rect.x,self.rect.y))
    def checkcollsion(self,player1):
        if self.rect.colliderect(player1):
            return True
            print("Collision")
        else:
            return False
class Bullet(object):
    def __init__(self):
        self.rect = pygame.Rect(player.rect.x+28,player.rect.y-8,8,16)
    def teleport(self,x1,y1):
        self.rect.x=x1
        self.rect.y=y1
    def draw(self):
        window.blit(bulletimg,(self.rect.x, self.rect.y))
    def move(self):
        self.rect.y-=2
class Row(object):
    def __init__(self):
        self.xmove=0.5
        self.rowy=0
        enemynum=0
        totalenemy = 5
        self.enemysprites=[]
        while enemynum < totalenemy:
            self.enemysprites.insert(enemynum, Enemy())
            self.enemysprites[enemynum].teleport(100*enemynum,self.rowy)
            enemynum+=1
            #print enemynum
    def changey(self,y):
        self.rowy=y
    def move(self):
        global running
        num=0
        for i in self.enemysprites:
            if i.checkcollsion(player) or i.x > 608:
                running = False
            if i.rect.colliderect(bullet):
                del self.enemysprites[num]
                bullet.rect.y=-16
            else:
                i.x=i.x+ self.xmove
                if i.x > 575.9 or i.x < 0.1:
                    changex(-self.xmove)
                i.teleport(i.x,self.rowy)
                i.draw()
            num=num+1
player = Player()
bullet = Bullet()
bullet.teleport(0,-16)
start=time.time()
createrows()
while running:
    window.fill((0,0,0))
    x,y=pygame.mouse.get_pos()
    player.teleport(x-32,560)
    bullet.move()
    player.draw()
    bullet.draw()
    for i in rows:
        i.move()
    num=0
    if pygame.mouse.get_pressed()[0] and bullet.rect.y < 1:
        bullet.teleport(x-4,player.rect.y-8)
    pygame.display.flip()
    frames+=1
    if frames > 119:
        timetaken=time.time()-start
        #print(str(frames/timetaken) + " FPS")
        start = time.time()
        frames=0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
