import pygame
import time
import random
from playsound import playsound
pygame.font.init()

WIDTH,HEIGHT = 1000,800
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Shooter")

P_HEIGHT = 40
P_WIDTH = 20

STAR_W = 10
STAR_H=40

 
FONT = pygame.font.SysFont("comicsans",30)

STAR_VEL = 1
PLAYER_VEL = 1

BG = pygame.transform.scale(pygame.image.load("bg.jpeg"),(WIDTH,HEIGHT))

def draw(player,elapsed,stars,lives):
    WIN.blit((BG),(0,0))

    init_val=30
    for i in range(lives):
        pygame.draw.circle(WIN,"red",(init_val+(i*100),100),20)
    

    timer = FONT.render("Timer: {}s".format(int(elapsed)),1,"white")

    for star in stars:
        pygame.draw.rect(WIN,"white",star)

    pygame.draw.rect(WIN,"red",player)
    
    WIN.blit(timer,(10,10))
    pygame.display.update()

def main():
    run = True
    lives =5

    star_add_increment=2000
    star_count=0
    stars=[]

    player = pygame.Rect(500,HEIGHT-P_HEIGHT,P_WIDTH,P_HEIGHT)

    clock =pygame.time.Clock()

    start_time=time.time()
    elapsed = 0
    

    while run==True:
        hit = False
        star_count+=clock.tick(240) 
        elapsed =time.time()- start_time

        if star_count>star_add_increment:
            for _ in range(5):
                star_x= random.randint(1,WIDTH-STAR_W)
                star = pygame.Rect(star_x,-STAR_H,STAR_W,STAR_H)
                stars.append(star)
            
            star_add_increment = max(200,star_add_increment-50)
            star_count=0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x-PLAYER_VEL >=0:
            player.x-=PLAYER_VEL
        
        if keys[pygame.K_RIGHT] and player.x+PLAYER_VEL <=WIDTH-P_WIDTH:
            player.x+=PLAYER_VEL
        
        if keys[pygame.K_UP] and player.y-PLAYER_VEL >=0:
            player.y-=PLAYER_VEL
        
        if keys[pygame.K_DOWN] and player.y+PLAYER_VEL <HEIGHT-P_HEIGHT:
            player.y+=PLAYER_VEL
        
        for star in stars[:]:
            star.y += STAR_VEL
            if star.x>HEIGHT:
                stars.remove(star)
            elif star.y + star.height>=player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break
        

        if hit:
            lives-=1
            if lives==0:
                lost_text = FONT.render("You Lost!",1,"White")
                WIN.blit(lost_text,(WIDTH/2 - lost_text.get_width()/2,HEIGHT/2 - lost_text.get_height()/2))
                pygame.display.update()
                pygame.time.delay(4000)
                break

        draw(player,elapsed,stars,lives)
    pygame.quit()

if __name__ == "__main__":
    main()
