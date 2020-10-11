import pygame
import random

pygame.init()

screen_Width = 1000
screen_height = 600

gwin=pygame.display.set_mode((screen_Width,screen_height))
# game colours
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

pygame.display.set_caption("Snakes with Abhi")
pygame.display.update()


# clock
clock=pygame.time.Clock()

 # screen score function
font = pygame.font.SysFont(0,55)

def plot_snake(gwin,color,snk_lst,s_size):
    for x,y in snk_lst:
        pygame.draw.rect(gwin,color,[x,y,s_size,s_size])

def  text_screen(text,color,x,y):
     screen_text = font.render(text,True,color)
     gwin.blit(screen_text, (x,y))


#Game loop

def gameloop():

    # Game specific variables
    exit_game = False
    Game_over = False
    snake_x = 45
    snake_y = 55
    # Velocities 
    v_x = 0
    v_y = 0
    init_v = 5

    s_size = 10
    fps = 20

    food_x= random.randint(20,screen_Width/2)
    food_y= random.randint(20,screen_height/2)
    score = 0
   
    snk_lst = []
    snk_len = 1
    while not exit_game:
        if Game_over:
            gwin.fill(white)
            text_screen("GAME OVER! PRESS ENTER TO CONTINUE",red,100,200)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else:    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        v_x = init_v
                        v_y = 0

                    if event.key == pygame.K_LEFT:
                        v_x = - init_v
                        v_y = 0

                    if event.key == pygame.K_UP:
                        v_y = -init_v
                        v_x = 0

                    if event.key == pygame.K_DOWN:
                        v_y = init_v
                        v_x = 0       

            snake_x += v_x
            snake_y += v_y

            if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
                score += 1
            # print ("Score :" , score*10)
                food_x= random.randint(20,screen_Width/2)
                food_y= random.randint(20,screen_height/2)    
                snk_len += 5

            gwin.fill(white)
            text_screen("Score: "+ str(score * 10),red,5,5)
            pygame.draw.rect(gwin,red,[food_x,food_y,s_size,s_size])

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_lst.append(head) 

            if len(snk_lst) > snk_len:
                del snk_lst[0]
            
            if head in snk_lst[:-1]:
                Game_over= True  
            if snake_x < 0 or snake_y < 0 or snake_x > screen_Width or snake_y > screen_height:
                Game_over = True
                print("GAME OVER")
            # pygame.draw.rect(gwin,black,[snake_x,snake_y,s_size,s_size])
            plot_snake(gwin,black,snk_lst,s_size)


        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
gameloop() 