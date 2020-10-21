import pygame
import random

pygame.init()

#colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)

#game-window
scw=900  #screen_width
sch=600   #screen_height
game_window=pygame.display.set_mode((scw,sch))

pygame.display.set_caption("har ek friend snake hota hai")
pygame.display.update()

font=pygame.font.SysFont(None,45)
def screen_score(text,color,x,y):  #screen_score
    screen_text=font.render(text,True,color)
    game_window.blit(screen_text,[x,y])

def plot_snake(game_window,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(game_window,color,[x,y,snake_size,snake_size])


#welcome screen
def welcome():
    exit_game=False
    while not exit_game:
        game_window.fill((56,56,56))
        screen_score("aagaya firse tu!",black,scw/4,sch/3)
        screen_score("spacebar daba agar khelna hai toh",red,scw/6,sch/2)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                    exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    game_loop()
        pygame.display.update()
                              #setting game fps
        clock=pygame.time.Clock()
        clock.tick(60)
#game-loop
def game_loop():
    #game-specific-variables
    exit_game=False
    game_over=False
    sx=40   #snake_x-location
    sy=50   #snake_y-location
    vx=0   #velocity_x
    vy=0   #velocity_y
    snake_size=20;d=0;V=5  #distance;velocity

    foodx=random.randint(20,scw/1.2) #food
    foody=random.randint(20,sch/1.2)

    score=0;snk_length=1;snk_list=[]  #score,snake list&length


    fps=50                      #setting game fps
    clock=pygame.time.Clock()
    while not exit_game:    
        if game_over:
            #game_window.fill(white)
            screen_score("SAANP MAR GAYA! chal enter daba firse khelna hai toh",red,scw/20,sch/3)
            #screen_score(f"score:{score}",red,scw/3,sch/2) 
            for event in pygame.event.get():         #event
                #print(event)
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:    
                    if event.key==pygame.K_RETURN:
                        game_loop()
                    else:
                        exit_game=True
        else:                     
            for event in pygame.event.get():         #event
                #print(event)
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        vx,vy=V,0
                        sx=sx+d
                    if event.key==pygame.K_LEFT:
                        vx,vy=-V,0
                        sx=sx-d
                    if event.key==pygame.K_UP:
                        vx,vy=0,-V
                        sy=sy-d
                    if event.key==pygame.K_DOWN:
                        vx,vy=0,+V
                        sy=sy+d
                    if event.key==pygame.K_SPACE:
                        vx,vy=0,0

            sx=sx+vx
            sy=sy+vy

            if abs(sx-foodx)<10 and abs(sy-foody)<10:
                score=score+10
                foodx=random.randint(20,scw/1.2)
                foody=random.randint(20,sch/1.2)
                snk_length+=5
            
            game_window.fill(white)
            screen_score("score :"+str(score),red,5,5)
            pygame.draw.rect(game_window,red,[foodx,foody,snake_size,snake_size])
            pygame.draw.rect(game_window,black,[sx,sy,snake_size,snake_size])

            head=[]
            head.append(sx)
            head.append(sy)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over=True

            if sx<0 or sy<0 or sx>scw or sy>sch:
                game_over=True 
                print("game_over")

            plot_snake(game_window,black,snk_list,snake_size)

        pygame.display.update()
        clock.tick(fps)



    pygame.quit()
    quit()
welcome()