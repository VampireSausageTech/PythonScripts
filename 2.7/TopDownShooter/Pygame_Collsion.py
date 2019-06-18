#Code by Jake Feeney
import pygame
pygame.font.init()
myfont = pygame.font.SysFont('Courier New', 150)
text=myfont.render('You Win', True, (225,0,0))
map0=[[1,1,1,1,1],
      [1,2,0,3,1],
      [1,1,1,1,1]]

map1=[[1,1,1,1,1],
    [1,0,0,2,1],
    [1,0,1,1,1],
    [1,0,0,3,1],
    [1,1,1,1,1]]
map2=[[1,1,1,1,1,1,1,1,1,1],
         [1,0,1,2,0,1,0,0,0,1],
         [1,0,1,1,0,0,1,1,0,1],
         [1,3,0,0,1,0,1,1,0,1],
         [1,0,1,0,1,0,0,1,0,1],
         [1,0,1,0,1,1,0,1,0,1],
         [1,0,1,0,0,0,0,1,0,1],
         [1,0,1,1,1,1,1,1,0,1],
         [1,0,0,0,0,0,0,0,0,1],
         [1,1,1,1,1,1,1,1,1,1]]
mapnum=0
maps=[map0, map1,map2]
def start(gamemap):
    num=0
    num2=0
    global blocklist, player, end, win
    win = False
    blocklist=[]
    for row in gamemap:
        for square in row:
            if square == 1:
                blocklist.insert(0,Block())
                blocklist[0].create(num,num2)
            elif square == 2:
                end=End()
                end.end(num,num2)
            elif square == 3:
                player=Player()
                player.player(num,num2)
            num=num+1
        num=0
        num2=num2+1
class End(object):
    def end(self,x,y):
        self.x=x*64
        self.y=y*64
        self.rect=pygame.Rect(self.x,self.y,64,64)
        pygame.draw.rect(window, (0,225,0), self.rect)
    def checkcollsion(self,player):
        if self.rect.colliderect(player.rect):
            return True
        else:
            return False
    def draw(self):
        pygame.draw.rect(window, (0,225,0), self.rect)
class Player(object):
    def player(self,x,y):
        self.x=x*64
        self.y=y*64
        self.x=self.x + 20
        self.y=self.y + 20
        self.rect=pygame.Rect(self.x,self.y,24,24)
        pygame.draw.rect(window, (0,0,225), self.rect)
    def move(self,xmove,ymove):
        self.x+=xmove
        self.y+=ymove
        self.rect=pygame.Rect(self.x,self.y,24,24)
    def draw(self):
        pygame.draw.rect(window, (0,0,225), self.rect)
    def teleport(x,y):
        self.x=x
        self.y=y
        self.rect=pygame.Rect(self.x,self.y,24,24)
class Block(object):
    def create(self,x,y):
        self.x=x*64
        self.y=y*64
        #print self.x
        self.rect=pygame.Rect(self.x,self.y,64,64)
        pygame.draw.rect(window,(225,0,0),self.rect)
    def checkcollsion(self,player):
        if self.rect.colliderect(player.rect):
            return True
        else:
            return False
    def draw(self):
        pygame.draw.rect(window, (225,0,0),self.rect)
window = pygame.display.set_mode((640,640), pygame.FULLSCREEN)
running = True
start(maps[mapnum])
while running:
    pygame.draw.rect(window,(0,0,0),(0,0,640,640))
    if end.checkcollsion(player):
        win=True
    key=pygame.key.get_pressed()
    xmove=0
    ymove=0
    if key[pygame.K_a]:
        xmove=-0.3
    elif key[pygame.K_d]:
        xmove=+0.3

    if key[pygame.K_w]:
        ymove=-0.3
    elif key[pygame.K_s]:
        ymove=0.3
    if key[pygame.K_ESCAPE]:
        running=False
    player.move(xmove,ymove)
    if win == False:
        for block in blocklist:
            if block.checkcollsion(player):
               player.move(-xmove,-ymove)
            block.draw()
        end.draw()
        player.draw()
    else:
        mapnum=mapnum+1
        if mapnum >= len(maps):
            window.blit(text, (320-text.get_width()//2,320-text.get_height()//2))
        else:
            start(maps[mapnum])
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
