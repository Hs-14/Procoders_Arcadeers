import turtle
import math
import random
import pygame

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("tank mazeme")
wn.setup(700, 700)
wn.tracer(0)
wn.register_shape('wall2.gif')
wn.register_shape('fuel.gif')
wn.register_shape('tankoppo.gif')
wn.register_shape('tankplay.gif')
wn.register_shape('door.gif')

def erasableWrite(tortoise, name, font, align, reuse= None):
    eraser = turtle.Turtle() if reuse is None else reuse
    eraser.hideturtle()
    eraser.up()
    eraser.setposition(-300,300)
    eraser.color("orange")
    eraser.write(name, font= font,align=align)
    return eraser

t = turtle.Turtle()

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('wall2.gif')
        self.color("grey")
        self.penup()
        self.speed(0)

class Door(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('door.gif')
        self.color("silver")
        self.penup()
        self.speed(0)

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('tankplay.gif')
        self.color("black")
        self.penup()
        self.speed(0)
        self.gold = 0

    def go_up(self):
        #calculate the spot to move
        move_to_x = player.xcor()
        move_to_y = player.ycor()+24

        #check if space has wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        #calculate the spot to move
        move_to_x = player.xcor()
        move_to_y = player.ycor()-24

        #check if space has wall
        if(move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)

    def go_left(self):
        # calculate the spot to move
        move_to_x = player.xcor()-24
        move_to_y = player.ycor()

        # check if space has wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        # calculate the spot to move
        move_to_x = player.xcor()+24
        move_to_y = player.ycor()

        # check if space has wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def in_collision(self,other):
        a=self.xcor()-other.xcor()
        b=self.ycor()-other.ycor()
        distance = math.sqrt((a ** 2)+(b**2))

        if distance < 5:
            return True
        else:
            return False



class Treasures(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape('fuel.gif')
        self.color("black")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x,y)

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()


class Enemy(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape('tankoppo.gif')
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x,y)
        self.direction = random.choice(["up","down","left","right"])
    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24

        elif self.direction == "down":
            dx = 0
            dy = -24

        elif self.direction == "left":
            dx = -24
            dy = 0

        elif self.direction == "right":
            dx = 24
            dy = 0

        else :
            dx = 0
            dy = 0


        #check player in class
        #if so, go in that dirn
        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction = "left"
            elif player.xcor > self.xcor():
                self.direction = "right"
            elif player.ycor < self.ycor():
                self.direction = "down"
            elif player.ycor > self.ycor():
                self.direction = "up"


        #calculate the spot to move
        move_to_x = self.xcor() +dx
        move_to_y = self.ycor() +dy

        #check if the space has a wall
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
        else:
            #choose different direction
            self.direction = random.choice(["up","down","left","right"])

        #set timer to more next time
        turtle.ontimer(self.move, t= random.randint(100,300))

    def is_close(self,other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a**2)+(b**2))

        if distance < 75:
            return True
        else:
            return False

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()



#create level list
levels = [""]





#define levels
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XO XXXXXXX         EXXXXX",
"X  XXXXXXX  XXXXXX  XXXXX",
"X       XX  XXXXXX  XXXXX",
"X       XX  XXX       EXX",
"XXXXXX  XX  XXX        XX",
"XXXXXX  XX  XXXXXX  XXXXX",
"XXXXXX  XX    XXXX  XXXXX",
"XG XXXE       XXXX GXXXXX",
"X  XXX  XXXXXXXXXXXXXXXXX",
"X         XXXXXXXXXXXXXXX",
"X E              XXXXXXXX",
"XXXXXXXXXXXX     XXXXX  X",
"XXXXXXXXXXXXXXX  XXXXX  X",
"XXX  XXXXXXXXXX         X",
"XXXE                    X",
"XXX         XXXXXXXXXXXXX",
"XXXXXXXXXX  XXXXXXXXXXXXX",
"XXXXXXXXXX              X",
"XX GXXXXXX  E           X",
"XX  XXXXXXXXXXXXXX  XXXXX",
"XX   DXXXXXXXXXXXX  XXXXX",
"XX E        XXXX        X",
"XXX                    GX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
]
#ADD TREASURE list
treasures = []

#add enemies
enemies = []

#add maze to maze list
levels.append(level_1)

#create level setup function
def setup_maze(level1):
    for y in range(len(level1)):
        for x in range(len(level1[y])):
            #get characters at each x,y coordinates
            #NOTE the order of y and x in next line
            character = level1[y][x]
            #calculate the screen x,y coordinates
            screen_x = -300 + (x*24)
            screen_y =  300 - (y*24)

            #check if it is an x (wall)
            if character == "X":
                pen.goto(screen_x,screen_y)
                pen.stamp()
                #add coordinates wall list
                walls.append((screen_x,screen_y))

            #check if it is an O(player)
            if character == "O":
                player.goto((screen_x),(screen_y))

            #check if its an G(treasure)
            if character == "G":
                treasures.append(Treasures(screen_x,screen_y))

            #check if its an E(enemy)
            if character == "E":
                enemies.append(Enemy(screen_x,screen_y))

            #check if  its an D(door)
            if character == "D":
                door.goto(screen_x,screen_y)


#create class instance
pen = Pen()
player = Player()
door = Door()

#create wall coordinate
walls = []

#setup the level
setup_maze(levels[1])

#keyboard binding
turtle.listen()
turtle.onkey(player.go_left,"a")
turtle.onkey(player.go_right,"d")
turtle.onkey(player.go_up,"w")
turtle.onkey(player.go_down,"s")

#turnoff screen updates

#start moving the enemies
for enemy in enemies:
    turtle.ontimer(enemy.move, t=250)



#main loop
while True:
    #check for the player collision
    #iterate through treasure list
    for treasure in treasures:
        if player.in_collision(treasure):
            #add treasure gold to player gold
            player.gold += treasure.gold
            print("Player Gold: ()".format(player.gold))
            #destroy the treasures
            treasure.destroy()

            #remove the treasure fron treasure list
            treasures.remove(treasure)

    #iterate through enemy list too see that player collide
    for enemy in enemies:
        if player.in_collision(enemy):
            player.gold -= 5
            print("Player Gold: ()".format(player.gold))

    if player.in_collision(door):
        print(" Your total score = ()".format(player.gold))
        break


    erasable = erasableWrite(t,player.gold,font=("Arial",20,"normal"),align="center")
    erasable.clear()
    #Update screen
    wn.update()