import pygame, time, call
pygame.init()
clock=pygame.time.Clock()

d_width=800
d_height=600

win=pygame.display.set_mode((d_width,d_height))
pygame.display.set_caption("Arcadeers")

game_icon=[]

# =============================================================================
#ALL CLASSES
class display(object):
    def msg_2_screen(msg,f_name,f_color,x_displace=0,y_displace=0,size=25,b=0,i=0,f_lcn=""):
        fonte=fontor(f_name,size,b,i,f_lcn)
        screen_text=fonte.render(msg,True,colour(f_color))
        win.blit(screen_text,
                 [(d_width/2)-screen_text.get_rect().width/2+x_displace,d_height/2+y_displace-screen_text.get_rect().height/2])
            
    def text_2_button(x,y,text,f_name,f_color,size=25,b=0,i=0,f_lcn=""):
        fonte=fontor(f_name,size,b,i,f_lcn)
        screen_text=fonte.render(text,True,colour(f_color))
        win.blit(screen_text,[x-screen_text.get_rect().width/2,y-screen_text.get_rect().height/2])
        
    def button(x,y,width,height,inactive,active,action=None,parameter=None):
        x=x-width/2
        y=y-height/2
        cur=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        if x<cur[0]<x+width and y<cur[1]<y+height:
            if parameter==None:
                pygame.draw.rect(win,colour(inactive),(x+3,y+3,width,height))
                pygame.draw.rect(win,colour(active),(x-3,y-3,width,height))
                if click[0]==1:
                    if click[0]==1 and action!=None:
                        if action=="quit":
                            1/0
                        elif action=="rules":
                            return False,"rules"
                        elif action=="play":
                            return False,"play"
                        elif action=="back":
                            return False,"intro"
                        elif action=="continue":
                            return False,None
                        else:
                            pass      
        else:
            pygame.draw.rect(win,colour(active),(x,y,width,height))
        return True,None
    
    def button1(i,x,y,parameter=None):
         #gName=['Prime','Demon','Dragon','Typhoon','Colossus']
         global l
         cur=pygame.mouse.get_pos()
         click=pygame.mouse.get_pressed()
         rect=game_icon[i].get_rect()
         x=x-rect.width/2
         y=y-rect.height/2
         win.blit(game_icon[i],(x,y))
         #display.msg_2_screen(gName[i],'agencyfb',colour('black'),x-d_width//2+game_icon[i].get_rect().width*80//140,y-d_height//2+game_icon[i].get_rect().height*3//2,game_icon[i].get_rect().height*3//4)
         if x<cur[0]<x+rect.width and y<cur[1]<y+rect.height:
             pygame.draw.rect(win,colour('grey'),(x-5,y-5,rect.width+10,rect.height+10),2)
             if click[0]:
                 l.append(1)
                 l.pop(0)
             else:
                 l.append(0)
                 l.pop(0)
             if l[-1]==0 and l[-2]==1:
                 time.sleep(0.1)
                 return parameter
             else:
                 return None
             

#############################################################################################################################################################################################
#ALL THE FUNCTIONS
def colour(colour):
    d_clr={"black":(0,0,0),
           "white":(255,255,255),
           "purple":(128,0,128),
           "green":(0,255,0),
           "cyan":(0,255,255),
           "yellow":(255,255,0),
           "magenta":(255,0,255),
           "red":(235,0,0),
           "b_green":(127,255,0),
           "lavender":(230,230,255),
           "orange":(255,127,80),
           "grey":(150,150,150),
           "blue":(0,0,255),
           "d_red":(175,0,0),
           "d_green":(0,150,0),
           "d_yellow":(175,175,0),
           "d_blue":(0,0,160),
           "d_grey":(100,100,100)}
    if type(colour)==tuple:
        return colour
    clr_code=d_clr[colour]
    return clr_code

def fontor(f_name="centurygothic",size=25,b=False,i=False,f_lcn=""):
    global font
    if len(f_lcn)==0:
        font=pygame.font.SysFont(str(f_name),size,b,i)
    else:
        f_lcn=f_lcn+"/"+f_name+'.ttf'
        font=pygame.font.Font(f_lcn,size,b,i)
    return font

 
# =============================================================================

def effects(colour,d="hl"):
    im_name="images/eff_"+colour+".png"
    img=pygame.image.load(im_name)
    if d[0]=="h":
        if d[1]=="l":
            img=img
        else:
            img=pygame.transform.rotate(img,180)
    elif d[0]:
        if d[1]=="u":
            img=pygame.transform.rotate(img,270)
        else:
            img=pygame.transform.rotate(img,90)
    else:
        pass
    return img

eff_red_hl=effects("red","hl")
eff_blue_hr=effects("blue","hr")
eff_white_vu=effects("white","vu")
eff_green_hl=effects("green","hl")
eff_cyan_vd=effects("cyan","vd")
eff_yellow_vd=effects("yellow","vd")
eff_magenta_vu=effects("magenta","vu")
eff_lavender_hr=effects("lavender","hr")
x=0
y=0

def intro():
    #intro
    i_cont=True
    i_cont1=True
    while i_cont and i_cont1:
        #cmd="play"
        win.fill(colour("black"))
        display.msg_2_screen("THE ULTIMATE GAME","centurygothic","grey",0,-150,60,True,True)
        display.msg_2_screen("For Arcadeers!!","chiller","red",0,-50,100,False,True)

        i_cont1,cmd1=display.button(int(d_width/2),int(0.7*d_height),120,60,"d_yellow","yellow","rules")
        i_cont,cmd=display.button(int(d_width/4),int(0.7*d_height),120,60,"d_green","green","play")
        display.button(int(d_width*3/4),int(0.7*d_height),120,60,"d_red","red","quit")
# =============================================================================
#         if cmd=="play":
#             i_cont=False            
# =============================================================================
        
        display.text_2_button(int(d_width/4),int(d_height*0.7),"PLAY","calibri","purple",35)
        display.text_2_button(int(d_width/2),int(0.7*d_height),"ABOUT","calibri","d_blue",35)
        display.text_2_button(int(d_width*3/4),int(0.7*d_height),"QUIT","calibri","black",35)
        
        global x
        global y
        win.blit(eff_blue_hr,(x-eff_red_hl.get_rect().width,30))
        win.blit(eff_red_hl,(d_width-x,50))
        win.blit(eff_green_hl,(d_width-x,d_height-30))
        win.blit(eff_lavender_hr,(x-eff_lavender_hr.get_rect().width,d_height-50))
        win.blit(eff_white_vu,(30,d_height-y))
        win.blit(eff_cyan_vd,(50,y-eff_cyan_vd.get_rect().height))
        win.blit(eff_yellow_vd,(d_width-30,y-eff_yellow_vd.get_rect().height))
        win.blit(eff_magenta_vu,(d_width-50,d_height-y))
        x+=2
        y+=2
        if x==d_width+eff_red_hl.get_rect().width:
            x=0
        if y==d_height+eff_white_vu.get_rect().height:
            y=0
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                1/0
            else:
                pass
        clock.tick(200)
        pygame.display.update()    
    if cmd==None:
        return cmd1
    else:
        return cmd

def rules():
    cont=True
    icont=True
    while cont and icont:        
        win.fill(colour('black'))
        
        display.msg_2_screen("A program with several Fun Games!",'Calibri',colour('red'),0,-200,size=40)
        display.msg_2_screen("Members:",'Cambria',colour('purple'),-150,-150,size=35)
        display.msg_2_screen("Harsh Verma",'Bookman Old Style',colour('green'),0,-110,size=35)
        display.msg_2_screen("Chaitanya Gupta",'Bookman Old Style',colour('green'),0,-60,size=35)
        display.msg_2_screen("Chaitany Raghav",'Bookman Old Style',colour('green'),0,-10,size=35)
        display.msg_2_screen("Dhairya Modi",'Bookman Old Style',colour('green'),0,40,size=35)
        
        
        
        cont,cmd=display.button(int(d_width/4),int(0.7*d_height),120,60,"blue","cyan","back")
        icont,cmd1=display.button(int(d_width/2),int(0.7*d_height),120,60,"d_green","green","play")
        display.button(int(d_width*3/4),int(0.7*d_height),120,60,"d_red","red","quit")
        display.text_2_button(int(d_width/4),int(d_height*0.7),"BACK","calibri","red",35)
        display.text_2_button(int(d_width/2),int(0.7*d_height),"PLAY","calibri","purple",35)
        display.text_2_button(int(d_width*3/4),int(0.7*d_height),"QUIT","calibri","black",35)
        
        global x
        global y
        win.blit(eff_blue_hr,(x-eff_red_hl.get_rect().width,30))
        win.blit(eff_red_hl,(d_width-x,50))
        win.blit(eff_green_hl,(d_width-x,d_height-30))
        win.blit(eff_lavender_hr,(x-eff_lavender_hr.get_rect().width,d_height-50))
        win.blit(eff_white_vu,(30,d_height-y))
        win.blit(eff_cyan_vd,(50,y-eff_cyan_vd.get_rect().height))
        win.blit(eff_yellow_vd,(d_width-30,y-eff_yellow_vd.get_rect().height))
        win.blit(eff_magenta_vu,(d_width-50,d_height-y))
        x+=2
        y+=2
        if x==d_width+eff_red_hl.get_rect().width:
            x=0
        if y==d_height+eff_white_vu.get_rect().height:
            y=0
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                1/0
            else:
                pass
        clock.tick(200)
        
        pygame.display.update()
    if cmd1==None:
        return cmd
    else:
        return cmd1

game_icon=[pygame.transform.scale(pygame.image.load('images/logos/angry_tictactoe.png'),(120,100)),
       pygame.transform.scale(pygame.image.load('images/logos/dots.png'),(150,100)),
       pygame.transform.scale(pygame.image.load('images/logos/pacman.png'),(100,100)),
       pygame.transform.scale(pygame.image.load('images/logos/snakes.png'),(130,100)),
       pygame.transform.scale(pygame.image.load('images/logos/sudoku.png'),(150,120)),
       pygame.transform.scale(pygame.image.load('images/logos/tank_trouble.png'),(100,100)),
       pygame.transform.scale(pygame.image.load('images/logos/tank.png'),(130,120))]

def play():
    cont=True
    while cont==True:
        win.fill(colour('black'))

        display.button(int(d_width*5/6),int(0.8*d_height),120,60,"d_red","red","quit")
        display.text_2_button(int(d_width*5/6),int(0.8*d_height),"QUIT","calibri","black",35)

        cmd_attt=display.button1(0,180,140,parameter='attt')
        cmd_dab=display.button1(1,400,140,parameter='dab')
        cmd_pm=display.button1(2,600,140,parameter='pm')
        cmd_s=display.button1(3,180,300,parameter='s')
        cmd_sdk=display.button1(4,400,300,parameter='sdk')
        cmd_tt=display.button1(5,600,300,parameter='tt')
        cmd_t=display.button1(6,300,470,parameter='t')
        display.text_2_button(180,212,"Angry TicTacToe",'Candara',colour('cyan'))
        display.text_2_button(400,210,"Dots and Boxes",'CG Omega',colour('red'),b=1)
        display.text_2_button(600,210,"Pac-Man",'digifacewide',colour('d_yellow'))
        display.text_2_button(180,372,'Snakes','Consolas',colour('green'))
        display.text_2_button(400,378,'SuDoKu','Helvetica',colour('purple'),b=1)
        display.text_2_button(600,372,'Tank Maze','Monaco',colour('orange'))
        display.text_2_button(415,470,'Tanks','Eurostile',colour('d_grey'),size=30)
        #stripe motion effect
        global x
        global y
        win.blit(eff_blue_hr,(x-eff_red_hl.get_rect().width,30))
        win.blit(eff_red_hl,(d_width-x,50))
        win.blit(eff_green_hl,(d_width-x,d_height-30))
        win.blit(eff_lavender_hr,(x-eff_lavender_hr.get_rect().width,d_height-50))
        win.blit(eff_white_vu,(30,d_height-y))
        win.blit(eff_cyan_vd,(50,y-eff_cyan_vd.get_rect().height))
        win.blit(eff_yellow_vd,(d_width-30,y-eff_yellow_vd.get_rect().height))
        win.blit(eff_magenta_vu,(d_width-50,d_height-y))
        x+=2
        y+=2
        if x==d_width+eff_red_hl.get_rect().width:
            x=0
        if y==d_height+eff_white_vu.get_rect().height:
            y=0
        
        #icon buttons
        
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                1/0
            else:
                pass
        clock.tick(200)
        pygame.display.update()
        
        ##launching game
        if cmd_attt!=None:
            print('opening')
            call.call(cmd_attt)
            cmd_attt=None
            time.sleep(0.5)
        elif cmd_dab!=None:
            call.call(cmd_dab)
            cmd_dab=None
            time.sleep(0.5)
        elif cmd_pm!=None:
            call.call(cmd_pm)
            cmd_pm=None
            time.sleep(0.5)
        elif cmd_s!=None:
            call.call(cmd_s)
            cmd_s=None
            time.sleep(0.5)
        elif cmd_sdk!=None:
            call.call(cmd_sdk)
            cmd_sdk=None
            time.sleep(0.5)
        elif cmd_tt!=None:
            call.call(cmd_tt)
            cmd_tt=None
            time.sleep(0.5)
        elif cmd_t!=None:
            call.call(cmd_t)
            cmd_t=None
            time.sleep(0.5)
        else:
            pass
    
run=True
cmd='intro'
try:
    l=[0,0,0,0,0,0,0,0,0,0]
    while run:
        if cmd=='intro':
            cmd=intro()
            time.sleep(0.15)
        elif cmd=='rules':
            cmd=rules()
            time.sleep(0.15)
        elif cmd=='play':
            cmd=play()
        else:
            pass
    
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
except Exception as e:
    print(e)
finally:
    del font
    pygame.display.quit()
    pygame.quit()

