import pygame
import random
from playsound import playsound
pygame.init()
pygame.font.init()
a=500
b=600

screen=pygame.display.set_mode((a,b))
#RGB  colorS

blue=(255,0,0)
red=(255,255,0)
white=(0,0,255)
pink=(255,255,255)

size=(25,20,10)

#FOOD
foodX=random.randrange(0,450)
foodY=random.randrange(50,500)

CAPTION=pygame.display.set_caption("snakegame-rahulAdhiari")
#sanke cordinate
snakeX=45
snakeY=55

score=0
clock=pygame.time.Clock()
snk_size=30

snk_list=[]
snk_length=1

def plot_snake(screen,color,snk_list,snk_size):
    for x,y in  snk_list:
        pygame.draw.rect(screen, color, [x, y, snk_size,snk_size])

velocityX=0
velocityY=0
font=pygame.font.Font("freesansbold.ttf",  40)

def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    screen.blit(screen_text,[0,0])

game=True
#gameloop
while  game:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game=False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                velocityX=-10
                velocityY=0
            if event.key==pygame.K_RIGHT:
                velocityX=10
                velocityY=0
            if event.key==pygame.K_UP:
                velocityY=-10
                velocityX=0
            if event.key==pygame.K_DOWN:
                velocityY = 10
                velocityX = 0
    snakeX=snakeX+velocityX
    snakeY=snakeY+velocityY
    if snakeX>=480  or  snakeX<=0 or snakeY>=580  or   snakeY<=0:
        game=False


    if abs(snakeX-foodX)<10 and abs(snakeY-foodY)<10:

        score=+1
        foodX=random.randrange(20,250)
        foodY=random.randrange(20,300)
        snk_length += 5
    screen.fill((0,255,0))

    text_screen("score: " + str(score  * 10),white,5,5)

    head=[]
    head.append(snakeX)
    head.append(snakeY)
    snk_list.append(head)

    if len(snk_list) > snk_length:
         del snk_list[0]
    plot_snake(screen, red, snk_list, snk_size)

    pygame.draw.rect(screen,blue,[foodX,foodY,snk_size,snk_size])
    pygame.display.update()
    clock.tick(60)

