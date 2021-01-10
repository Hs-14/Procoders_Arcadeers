import random
import pygame
import math
import time

# Initializing Pygame
pygame.init()

# Clock
clock = pygame.time.Clock()
FPS = -1

# Screen     '''                  can change these parameters                  '''
width = 150
line_width = 3
message_window = 40
end_fontsize = 40
ROWS = 3  # Don't change for best experience

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (128, 0, 128)
cyan = (0, 255, 255)
yellow = (255, 255, 0)
magenta = (255, 0, 255)
b_green = (127, 255, 0)
lavender = (230, 230, 255)
orange = (255, 127, 80)
grey = (150, 150, 150)
d_red = (175, 0, 0)
d_green = (0, 150, 0)
d_yellow = (175, 175, 0)
d_blue = (0, 0, 160)
d_grey = (100, 100, 100)

# Set Colour '''                  can change these parameters                  '''
end_text_colour = green
line_colour = gray
background_colour = white
window_text_colour = green
message_window_colour = black
end_window_message_colour = black

# Dependent Parameters
display_width = width * ROWS + line_width * (ROWS - 1)
win = pygame.display.set_mode((display_width, display_width + message_window))
pygame.display.set_caption("TicTacToe")
img_size = (3 * width) // 4
message_window_fontsize = (3 * message_window) // 4

# Images
X_IMAGE = pygame.transform.scale(pygame.image.load('Angry_Tictactoe/'+"Player1.png"), (img_size, img_size))
O_IMAGE = pygame.transform.scale(pygame.image.load('Angry_Tictactoe/'+"Player2.png"), (img_size, img_size))
Background_IMAGE = pygame.transform.scale(pygame.image.load('Angry_Tictactoe/'+"Background.png"), (display_width, display_width))

# Fonts
END_FONT = pygame.font.SysFont('courier', end_fontsize)
MESSAGE_FONT = pygame.font.SysFont('courier', message_window_fontsize)

global score_p1, score_p2
score_p1 = 0
score_p2 = 0


def draw_grid():
    gap = display_width // ROWS
    # Starting points
    x = 0
    y = 0

    for i in range(ROWS):
        x = i * gap

        pygame.draw.line(win, line_colour, (x, 0), (x, display_width), line_width)
        pygame.draw.line(win, line_colour, (0, x), (display_width, x), line_width)


def initialize_grid():
    dis_to_cen = display_width // ROWS // 2

    # Initializing the array
    game_array = [[None, None, None], [None, None, None], [None, None, None]]

    for i in range(len(game_array)):
        for j in range(len(game_array[i])):
            x = dis_to_cen * (2 * j + 1)
            y = dis_to_cen * (2 * i + 1)

            # Adding centre coordinates
            game_array[i][j] = (x, y, "", True)

    return game_array


def click(game_array):
    global P1_turn, P2_turn, images

    # Mouse position
    m_x, m_y = pygame.mouse.get_pos()

    for i in range(len(game_array)):
        for j in range(len(game_array[i])):
            x, y, char, can_play = game_array[i][j]

            # Distance between mouse and the centre of the square
            dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)

            # If it's inside the square
            if dis < display_width // ROWS // 2 and can_play:
                if P1_turn:  # If it's X's turn
                    images.append((x, y, X_IMAGE))
                    P1_turn = False
                    P2_turn = True
                    game_array[i][j] = (x, y, 'Player 1', False)

                elif P2_turn:  # If it's O's turn
                    images.append((x, y, O_IMAGE))
                    P1_turn = True
                    P2_turn = False
                    game_array[i][j] = (x, y, 'Player 2', False)


# Checking if someone has won
def has_won(game_array):
    winner = ' '
    global score_p1, score_p2
    # Checking rows
    for row in range(len(game_array)):
        if (game_array[row][0][2] == game_array[row][1][2] == game_array[row][2][2]) and game_array[row][0][2] != "":
            display_message(game_array[row][2][2].upper() + " has won!")
            winner = game_array[row][2][2]
            if winner == 'Player 1':
                score_p1 += 1
            elif winner == 'Player 2':
                score_p2 += 1
            return True

    # Checking columns
    for col in range(len(game_array)):
        if (game_array[0][col][2] == game_array[1][col][2] == game_array[2][col][2]) and game_array[0][col][2] != "":
            display_message(game_array[0][col][2].upper() + " has won!")
            winner = game_array[0][col][2]
            if winner == 'Player 1':
                score_p1 += 1
            elif winner == 'Player 2':
                score_p2 += 1
            return True

    # Checking main diagonal
    if (game_array[0][0][2] == game_array[1][1][2] == game_array[2][2][2]) and game_array[0][0][2] != "":
        display_message(game_array[0][0][2].upper() + " has won!")
        winner = game_array[0][0][2]
        if winner == 'Player 1':
            score_p1 += 1
        elif winner == 'Player 2':
            score_p2 += 1
        return True

    # Checking reverse diagonal
    if (game_array[0][2][2] == game_array[1][1][2] == game_array[2][0][2]) and game_array[0][2][2] != "":
        display_message(game_array[0][2][2].upper() + " has won!")
        winner = game_array[0][2][2]
        if winner == 'Player 1':
            score_p1 += 1
        elif winner == 'Player 2':
            score_p2 += 1
        return True

    return False


def has_drawn(game_array):
    for i in range(len(game_array)):
        for j in range(len(game_array[i])):
            if game_array[i][j][2] == "":
                return False

    display_message("It's a draw!")
    return True


def display_message(content):
    pygame.time.delay(500)
    win.fill(black)
    # win.blit(Background_IMAGE, (0, 0))
    end_text = END_FONT.render(content, True, end_text_colour)
    # pygame.draw.rect(win, end_window_message_colour, (((display_width - end_text.get_width()) // 2, (display_width - end_text.get_height()) // 2), end_text.get_width(), end_text.get_height() ))
    win.blit(end_text, ((display_width - end_text.get_width()) // 2, (display_width - end_text.get_height()) // 2))
    pygame.display.update()
    pygame.time.delay(3000)


def render():
    global P1_turn, P2_turn
    win.fill(background_colour)
    win.blit(Background_IMAGE, (0, 0))
    draw_grid()
    pygame.draw.rect(win, message_window_colour, (0, display_width, display_width, message_window))
    # Drawing X's and O's
    for image in images:
        x, y, IMAGE = image
        win.blit(IMAGE, (x - IMAGE.get_width() // 2, y - IMAGE.get_height() // 2))
    if P1_turn:
        message_text = MESSAGE_FONT.render("Player 1's Turn", True, window_text_colour)
    else:
        message_text = MESSAGE_FONT.render("Player 2's Turn", True, window_text_colour)
    win.blit(message_text, ((display_width - message_text.get_width()) // 2,
                            display_width + ((message_window - message_text.get_height()) // 2)))
    pygame.display.update()


def main():
    global P1_turn, P2_turn, images, draw, gameOver

    images = []
    draw = False

    run = True

    x = random.randint(0, 1)
    if x == 0:
        P1_turn = True
        P2_turn = False
    else:
        P2_turn = True
        P1_turn = False

    game_array = initialize_grid()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click(game_array)

        render()

        if has_won(game_array) or has_drawn(game_array):
            run = False
            gameOver = not run
        if FPS != -1:
            clock.tick(FPS)




def gameLoop():
    global gameOver, gameExit
    gameExit = False
    gameOver = False
    main()
    while not gameExit:
        while gameOver == True:
            win.fill(black)
            rules()



#################################################### The UI STUFF ####################################################################################
d_width = display_width
d_height = display_width

game_icon = []


# =============================================================================
# ALL CLASSES
class display(object):
    def msg_2_screen(msg, f_name, f_color, x_displace=0, y_displace=0, size=25, b=0, i=0, f_lcn=""):
        fonte = fontor(f_name, size, b, i, f_lcn)
        screen_text = fonte.render(msg, True, colour(f_color))
        win.blit(screen_text,
                 [(d_width / 2) - screen_text.get_rect().width / 2 + x_displace,
                  d_height / 2 + y_displace - screen_text.get_rect().height / 2])

    def text_2_button(x, y, text, f_name, f_color, size=25, b=0, i=0, f_lcn=""):
        fonte = fontor(f_name, size, b, i, f_lcn)
        screen_text = fonte.render(text, True, colour(f_color))
        win.blit(screen_text, [x - screen_text.get_rect().width / 2, y - screen_text.get_rect().height / 2])

    def button(x, y, width, height, inactive, active, action=None, parameter=None):
        x = x - width / 2
        y = y - height / 2
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < cur[0] < x + width and y < cur[1] < y + height:
            if parameter == None:
                pygame.draw.rect(win, colour(inactive), (x + 3, y + 3, width, height))
                pygame.draw.rect(win, colour(active), (x - 3, y - 3, width, height))
                if click[0] == 1:
                    if click[0] == 1 and action != None:
                        if action == "quit":
                            1 / 0
                        elif action == "rules":
                            return False, "rules"
                        elif action == "play":
                            return False, "play"
                        elif action == "back":
                            return False, "intro"
                        elif action == "continue":
                            return False, None
                        else:
                            pass
        else:
            pygame.draw.rect(win, colour(active), (x, y, width, height))
        return True, None

    def button1(i, x, y, parameter=None, t=0):
        gName = ['Prime', 'Demon', 'Dragon', 'Typhoon', 'Colossus']
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        rect = game_icon[i].get_rect()
        x = x - rect.width / 2
        y = y - rect.height / 2
        win.blit(game_icon[i], (x, y))
        display.msg_2_screen(gName[i], 'agencyfb', colour('black'),
                             x - d_width // 2 + game_icon[i].get_rect().width * 80 // 140,
                             y - d_height // 2 + game_icon[i].get_rect().height * 3 // 2,
                             game_icon[i].get_rect().height * 3 // 4)
        if x < cur[0] < x + rect.width and y < cur[1] < y + rect.height:
            pygame.draw.rect(win, colour('grey'), (x - 5, y - 5, rect.width + 10, rect.height + 10), 2)
            if click[0]:
                return parameter


#############################################################################################################################################################################################
# ALL THE FUNCTIONS
def colour(colour):
    d_clr = {"black": (0, 0, 0),
             "white": (255, 255, 255),
             "purple": (128, 0, 128),
             "green": (0, 255, 0),
             "cyan": (0, 255, 255),
             "yellow": (255, 255, 0),
             "magenta": (255, 0, 255),
             "red": (235, 0, 0),
             "b_green": (127, 255, 0),
             "lavender": (230, 230, 255),
             "orange": (255, 127, 80),
             "grey": (150, 150, 150),
             "blue": (0, 0, 255),
             "d_red": (175, 0, 0),
             "d_green": (0, 150, 0),
             "d_yellow": (175, 175, 0),
             "d_blue": (0, 0, 160),
             "d_grey": (100, 100, 100)}
    if type(colour) == tuple:
        return colour
    clr_code = d_clr[colour]
    return clr_code


def fontor(f_name="centurygothic", size=25, b=False, i=False, f_lcn=""):
    global font
    if len(f_lcn) == 0:
        font = pygame.font.SysFont(str(f_name), size, b, i)
    else:
        f_lcn = f_lcn + "\\" + f_name
        font = pygame.font.Font(f_lcn, size, b, i)
    return font


# =============================================================================

def effects(colour, d="hl"):
    im_name = "images/eff_" + colour + ".png"
    img = pygame.image.load('Angry_Tictactoe/'+im_name)
    if d[0] == "h":
        if d[1] == "l":
            img = img
        else:
            img = pygame.transform.rotate(img, 180)
    elif d[0]:
        if d[1] == "u":
            img = pygame.transform.rotate(img, 270)
        else:
            img = pygame.transform.rotate(img, 90)
    else:
        pass
    return img


eff_red_hl = effects("red", "hl")
eff_blue_hr = effects("blue", "hr")
eff_white_vu = effects("white", "vu")
eff_green_hl = effects("green", "hl")
eff_cyan_vd = effects("cyan", "vd")
eff_yellow_vd = effects("yellow", "vd")
eff_magenta_vu = effects("magenta", "vu")
eff_lavender_hr = effects("lavender", "hr")
x = 0
y = 0


################################ First page ###########################
def intro():
    # intro
    i_cont = True
    i_cont1 = True
    while i_cont and i_cont1:
        # cmd="play"
        win.fill(colour("black"))
        display.msg_2_screen("TIC TAC TOE", "centurygothic", "grey", 0, -100, 50, True, True)
        # display.msg_2_screen("For Arcadeers!!", "chiller", "red", 0, -50, 100, False, True)

        # i_cont1, cmd1 = display.button(int(d_width / 2), int(0.7 * d_height), 120, 60, "d_yellow", "yellow", "rules")
        i_cont, cmd = display.button(int(d_width / 3), int(0.7 * d_height), 120, 60, "d_green", "green", "play")
        display.button(int(d_width * 2 / 3), int(0.7 * d_height), 120, 60, "d_red", "red", "quit")
        # =============================================================================
        #         if cmd=="play":
        #             i_cont=False
        # =============================================================================

        display.text_2_button(int(d_width / 3), int(d_height * 0.7), "PLAY", "calibri", "purple", 35)
        # display.text_2_button(int(d_width / 2), int(0.7 * d_height), "ABOUT", "calibri", "d_blue", 35)
        display.text_2_button(int(d_width * 2 / 3), int(0.7 * d_height), "QUIT", "calibri", "black", 35)
        #########################all the effects in main page###########################################
        global x
        global y
        win.blit(eff_blue_hr, (x - eff_red_hl.get_rect().width, 30))
        win.blit(eff_red_hl, (d_width - x, 50))
        win.blit(eff_green_hl, (d_width - x, d_height - 30))
        win.blit(eff_lavender_hr, (x - eff_lavender_hr.get_rect().width, d_height - 50))
        win.blit(eff_white_vu, (30, d_height - y))
        win.blit(eff_cyan_vd, (50, y - eff_cyan_vd.get_rect().height))
        win.blit(eff_yellow_vd, (d_width - 30, y - eff_yellow_vd.get_rect().height))
        win.blit(eff_magenta_vu, (d_width - 50, d_height - y))
        x += 2
        y += 2
        if x == d_width + eff_red_hl.get_rect().width:
            x = 0
        if y == d_height + eff_white_vu.get_rect().height:
            y = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                1 / 0
            else:
                pass
        clock.tick(200)
        pygame.display.update()
        #######################################################################

    return cmd


################################ END OF FIRST PAGE ##############################

############################## Last Page ##################################
def rules():
    global gameExit, gameOver
    cont = True
    icont = True
    while cont and icont:
        win.fill(colour("black"))
        display.msg_2_screen("PLAYER 1:" + str(score_p1), "centurygothic", "grey", 0, -130, 25, True, True)
        display.msg_2_screen("PLAYER 2:" + str(score_p2), "centurygothic", "grey", 0, -105, 25, True, True)

        # cont, cmd = display.button(int(d_width / 4), int(0.7 * d_height), 120, 60, "blue", "cyan", "back")
        icont, cmd1 = display.button(int(d_width / 3), int(0.7 * d_height), 120, 60, "d_green", "green", "play")
        display.button(int(d_width * 2 / 3), int(0.7 * d_height), 120, 60, "d_red", "red", "quit")
        # display.text_2_button(int(d_width / 4), int(d_height * 0.7), "BACK", "calibri", "red", 35)
        display.text_2_button(int(d_width / 3), int(0.7 * d_height), "PLAY AGAIN", "calibri", "purple", 20)
        display.text_2_button(int(d_width * 2 / 3), int(0.7 * d_height), "QUIT", "calibri", "black", 35)
        #time.sleep(10)
        ##############all the effects on about page##################################
        global x
        global y
        win.blit(eff_blue_hr, (x - eff_red_hl.get_rect().width, 30))
        win.blit(eff_red_hl, (d_width - x, 50))
        win.blit(eff_green_hl, (d_width - x, d_height - 30))
        win.blit(eff_lavender_hr, (x - eff_lavender_hr.get_rect().width, d_height - 50))
        win.blit(eff_white_vu, (30, d_height - y))
        win.blit(eff_cyan_vd, (50, y - eff_cyan_vd.get_rect().height))
        win.blit(eff_yellow_vd, (d_width - 30, y - eff_yellow_vd.get_rect().height))
        win.blit(eff_magenta_vu, (d_width - 50, d_height - y))
        x += 2
        y += 2
        if x == d_width + eff_red_hl.get_rect().width:
            x = 0
        if y == d_height + eff_white_vu.get_rect().height:
            y = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                1 / 0
            else:
                pass
        clock.tick(200)

        pygame.display.update()
        ################################################################
    if cmd1 == "play":
        gameExit = False
        gameOver = True
        gameLoop()
        rules()
    return cmd1


##################################### End of last page #################################

l = [(d_width // 2, d_height // 2), (d_width // 4, d_height // 3), (d_width * 3 // 4, d_height // 3),
     (d_width // 4, d_height * 2 // 3), (d_width * 3 // 4, d_height * 2 // 3)]


################################## play function #################################################
def play():
    gameLoop()
    rules()

################################## End of play function ##########################################

######################################## DRIVER CODE ###############################
run = True
cmd = 'intro'
try:
    while run:
        if cmd == 'intro':
            cmd = intro()
            time.sleep(0.15)
        elif cmd == 'rules':
            cmd = rules()
            time.sleep(0.15)
        elif cmd == 'play':
            cmd = play()
        else:
            pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
except Exception as e:
    print(e)
finally:
    del font
    pygame.display.quit()
    pygame.quit()
################################## END OF DRIVER CODE ########################################
################################################### END OF UI STUFF #################################################