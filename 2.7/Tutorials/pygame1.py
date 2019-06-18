import pygame

pygame.init()
window=pygame.display.set_mode((640,640))
block1=pygame.Rect(0,100,100,100)
running = True
x=0
y=100
xmove=1
ymove=1
while running:
    pygame.draw.rect(window, (0,0,0), (0,0,640,640))
    pygame.draw.rect(window, (225,0,0), block1)
    block1=pygame.Rect(x,y,100,100)
    x+=xmove
    y+=ymove
    pygame.display.flip()
    if x == 540 or x == 0:
        xmove=-xmove
    if y == 540 or y == 0:
        ymove=-ymove
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

