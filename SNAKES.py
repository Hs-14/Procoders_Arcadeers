import pygame
import time
import random

pygame.init()

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,125,0)
blue=(0,0,125)
d_width=800
d_height=600
block_size=10
global fps
fps=20
y=0
smallfont=pygame.font.SysFont("comicsansms",25)
medfont=pygame.font.SysFont("comicsansms",50)
bigfont=pygame.font.SysFont("comicsansms",100)
font1=pygame.font.SysFont(None,40,True,True)
font2=pygame.font.SysFont(None,100,False,True)

icon=pygame.image.load('python_snake/apple.png')
pygame.display.set_icon(icon)

dir_n="right"

clock=pygame.time.Clock()

gamedisplay=pygame.display.set_mode((d_width,d_height))
pygame.display.set_caption('Slither')

def game_intro():
    intro=True
    while intro:
        gamedisplay.fill(white)
        msg_2_screen("Welcome!! to Slither",
                     green,
                     -100,
                     size="medium")
        msg_2_screen("The objective of the game is to eat red apples.",
                     black,
                     0,
                     "small")
        msg_2_screen("The more apples you eat the longer you get.",
                     black,
                     30,
                     "small")
        msg_2_screen("but watchout! cuz the more you score the faster Slither gets.",
                     black,
                     60,
                     "small")
        msg_2_screen("And obviously do not try to run into yourself or go offscreen.",
                     black,
                     90,
                     "small")
        msg_2_screen("Press C to play or Q to quit.",
                     black,
                     180,
                     "small")
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                1/0
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    intro=False
                elif event.key==pygame.K_q:
                    1/0
                else:
                   pass 
def pause():
    i=1
    while i>0:
        paused=font2.render("PAUSED",True,black)
        gamedisplay.blit(paused,[(d_width/2)-(len("paused")/2)*50,d_height/2-30])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                1/0
            if event.type==pygame.KEYDOWN:
                i=-1
        

def FPS(fps):
    fps_text=smallfont.render("FPS: "+str(fps),True,black)
    gamedisplay.blit(fps_text,[10,10])

def msg_2_screen(msg,color,y_displace=0,size="small"):
    if size=="small":
        screen_text=smallfont.render(msg,True,color)
        gamedisplay.blit(screen_text,
                         [(d_width/2)-(len(msg)/2)*11.75,d_height/2+y_displace])
    elif size=="medium":
        screen_text=medfont.render(msg,True,color)
        gamedisplay.blit(screen_text,
                         [(d_width/2)-(len(msg)/2)*25,d_height/2+y_displace])
    else:
        screen_text=bigfont.render(msg,True,color)
        gamedisplay.blit(screen_text,
                         [(d_width/2)-(len(msg)/2)*40,d_height/2+y_displace])

r_apple_image=pygame.image.load('python_snake/apple.png')
apple_thickness=30
def r_apple():
    r_apple_x=random.randrange(0,d_width-apple_thickness)
    r_apple_y=random.randrange(0,d_height-apple_thickness)
    return r_apple_x,r_apple_y
s_head_image=pygame.image.load('python_snake/snake_head.png')
s_body_image=pygame.image.load('python_snake/snake_body.png')
s_tail_image=pygame.image.load('python_snake/snake_tail.png')
def snake(block_size,snakelist):
    if lead_x_change==block_size:
        head=pygame.transform.rotate(s_head_image, 270)
    elif lead_x_change==-block_size:
        head=pygame.transform.rotate(s_head_image, 90)
    elif lead_y_change==-block_size:
        head=pygame.transform.rotate(s_head_image, 0)
    else:
        head=pygame.transform.rotate(s_head_image, 180)
    if len(snakelist)>=2:    
        tail_x_change=snakelist[1][0]-snakelist[0][0]
        tail_y_change=snakelist[1][1]-snakelist[0][1]
        if tail_x_change==block_size:
            tail=pygame.transform.rotate(s_tail_image, 270)
        elif tail_x_change==-block_size:
            tail=pygame.transform.rotate(s_tail_image, 90)
        elif tail_y_change==-block_size:
            tail=pygame.transform.rotate(s_tail_image, 0)
        else:
            tail=pygame.transform.rotate(s_tail_image, 180)
        
    for xy in snakelist:
        if snakelist.index(xy)==len(snakelist)-1:
            gamedisplay.blit(head,[xy[0],xy[1]])
        elif snakelist.index(xy)==0:
            gamedisplay.blit(tail,[xy[0],xy[1]])
        else:
            gamedisplay.blit(s_body_image,[xy[0],xy[1]])
            
def score(score):
    scr="Score: "+str(score)
    score_display=font1.render(scr,True,black)           
    gamedisplay.blit(score_display,[d_width-len(scr)*20,25])

#MAINLOOP
def gameLoop():
    gameExit=False
    gameOver=False
    lead_x=d_width/2
    lead_y=d_height/2
    global lead_x_change
    global lead_y_change
    lead_x_change=10
    lead_y_change=0
    snakelist=[]
    snakelength=1
    r_apple_x,r_apple_y=r_apple()
    while not gameExit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                1/0
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    lead_x_change=-block_size
                    lead_y_change=0
                elif event.key==pygame.K_RIGHT:
                    lead_x_change=+block_size
                    lead_y_change=0
                elif event.key==pygame.K_UP:
                    lead_y_change=-block_size
                    lead_x_change=0
                elif event.key==pygame.K_DOWN:
                    lead_y_change=+block_size
                    lead_x_change=0
                else:
                    pass
                if event.key==pygame.K_p:
                    pause()
            '''if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    lead_x_change=0
                if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                    lead_y_change=0'''
        lead_x+=lead_x_change
        lead_y+=lead_y_change
        
        if lead_x>=d_width or lead_x<0 or lead_y>=d_height or lead_y<0:
            gamedisplay.fill(red)
            msg1="you have hit the wall"
            msg_2_screen(msg1,black)
            pygame.display.update()
            time.sleep(1.5)
            gameOver=True
            
        gamedisplay.fill(white)
        gamedisplay.blit(r_apple_image,[r_apple_x,r_apple_y])
                
        snakehead=[]
        snakehead.extend([lead_x,lead_y])
        snakelist.append(snakehead)
        if len(snakelist)>snakelength:
            del snakelist[0]
        
        snake(block_size,snakelist)

        if snakelist[-1] in snakelist[:-1]:
            gamedisplay.fill(red)
            msg2="you ran into yourself"
            msg_2_screen(msg2,black)
            pygame.display.update()
            time.sleep(1.5)
            gameOver=True
        global fps
        FPS(fps)
        score(snakelength-1)
        pygame.display.update()
        
        
# =============================================================================
#         if lead_x+block_size/2>=r_apple_x and lead_x+block_size/2<r_apple_x+apple_thickness:
#             if lead_y+block_size/2>=r_apple_y and lead_y+block_size/2<r_apple_y+apple_thickness:
#                 r_apple()
#                 snakelength+=1
# =============================================================================
        
        if (lead_x>r_apple_x and lead_x<r_apple_x+apple_thickness) or (lead_x+block_size>r_apple_x and lead_x+block_size<r_apple_x+apple_thickness):
            if (lead_y>r_apple_y and lead_y<r_apple_y+apple_thickness) or (lead_y+block_size>r_apple_y and lead_y+block_size<r_apple_y+apple_thickness):
                r_apple_x,r_apple_y=r_apple()
                snakelength+=1
        
        while gameOver==True:
                gamedisplay.fill(red)
                G_O='Game Over'
                C_or_Q='Press C to continue or Q to quit'
                FPS(fps)
                score(snakelength-1)
                msg_2_screen(G_O,
                             blue,
                             y_displace=-50,
                             size="medium")
                msg_2_screen(C_or_Q,
                             black,
                             50,
                             size="small")
                pygame.display.update()
                
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                            1/0
                    elif event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_q:
                            1/0
                        elif event.key==pygame.K_c:
                            fps=20
                            global y
                            y=0
                            gameLoop()
                        else:
                            pass
                    else:
                        pass
        
        if (snakelength-1)%5==0 and snakelength-1>y:
            y+=5
            fps+=5
        clock.tick(fps)          
try:
    game_intro()   
    gameLoop()
except:
    del smallfont
    del medfont
    del bigfont
    del font1
    del font2
pygame.display.quit()
pygame.quit()