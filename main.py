#Libraries used
import pygame,sys
import numpy as np

#initializing
pygame.init()

#Screen resolution
Width = Height = 600

#Screen attributes
S_color = (255,153,153)
screen = pygame.display.set_mode((Width,Height))
screen.fill(S_color)
pygame.display.set_caption('TIC-TAC-TOE')

#Line attributes
Line_color = (110,110,110)
Line_width = 13

#Main-board
Board_rows = Board_cols = 3
board = np.zeros((Board_rows,Board_cols))
square_size = Width // Board_cols

#Figures-attributes
circle_rad = square_size//3
circle_wid = 15
circle_color = (64,64,64)
cross_color = (255,255,255)
cross_width = 15
space = square_size//4


def line_drawer():
    pygame.draw.line(screen, Line_color, (0, square_size), (Width, square_size), Line_width)  #First-Horizontal line
    pygame.draw.line(screen, Line_color, (0, 2*square_size), (Width, 2*square_size), Line_width)  #Second-Horizontal line
    pygame.draw.line(screen, Line_color, (square_size, 0), (square_size, Height), Line_width)  #First-Vertical line
    pygame.draw.line(screen, Line_color, (2*square_size, 0), (2*square_size, Height), Line_width)  #Second-vertical line
    pass



#To make the tic-tac-toe grid
def playing_field():
    line_drawer()

#To mark a square on board
def mark_boardsq(row,col,player):
    board[row][col] = player

#To check whether a particular square is available for marking
def square_avaialble(row,col):
    return board[row][col] == 0

#To check if the board is fully filled or not
def is_board_full():
    for i in range(Board_rows):
        for j in range(Board_cols):
            if board[i][j] == 0:
                return False
    return True

Ffont = pygame.font.SysFont('monotypecorsiva', 50)
def text_to_screen(screen, text, x, y, color,size = 50, font_type = Ffont):
        text = str(text)
        text = Ffont.render(text, True, color)
        screen.blit(text, (x, y))


def draw_shapes():
    for row in range(Board_rows):
        for col in range(Board_cols):
            if board[row][col] == 1:
                pygame.draw.circle(screen,circle_color,(int(row * square_size + square_size//2),int(col*square_size + square_size//2)),circle_rad,circle_wid)
            elif board[row][col] == 2:
                pygame.draw.line(screen,cross_color,(row*square_size+space,col*square_size+square_size-space),(row*square_size+square_size-space,col*square_size+space),cross_width)
                pygame.draw.line(screen,cross_color,(row*square_size+space,col*square_size + space),(row*square_size+square_size-space,col*square_size+square_size-space),cross_width)



def win_check(player):
    #Vertical check
    for col in range(Board_cols):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_horizontal_winline(col,player)
            return True

    #Horizontal check
    for row in range(Board_rows):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_vertical_winline(row,player)
            return True
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_winline(player)
        return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_winline(player)
        return True
    return  False

def draw_vertical_winline(col,player):
    Xpos = col*square_size + square_size//2

    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color
    pygame.draw.line(screen,color,(Xpos,15),(Xpos,Height-15),15)

def draw_horizontal_winline(row,player):
    Ypos = row * square_size + square_size//2

    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color

    pygame.draw.line(screen, color, (15, Ypos), (Width -15,Ypos), 15)

def draw_asc_winline(player):
    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color

    pygame.draw.line(screen,color,(15,Height-15),(Width-15,15),15)

def draw_desc_winline(player):
    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color

    pygame.draw.line(screen, color, (15, 15), (Width - 15, Height - 15), 15)


#Main window

def main_screen():
    #Player-profiles
    playing = True
    player = 1
    game_life = False
    while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        playing = True
                        reset()
                    elif event.key == pygame.K_r:
                        reset()
                        game_life = False
                    elif event.key == pygame.K_q:
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and not game_life:
                    Click_x = event.pos[0]
                    Click_y = event.pos[1]
                    print('playing: ',playing)

                    Corx = int(Click_x // square_size)
                    Cory = int(Click_y // square_size)

                    print('X: ',Corx)
                    print('Y: ',Cory)

                    if square_avaialble(Corx,Cory):
                        mark_boardsq(Corx,Cory,player)
                        if win_check(player):
                            game_life = True
                            #wonn(player)
                        player = player % 2 + 1
                        draw_shapes()
            pygame.display.update()

def reset():
    screen.fill(S_color)
    line_drawer()
    for row in range(Board_rows):
        for cols in range(Board_cols):
            board[row][cols] = 0
    main_screen()

def wonn(player):

    screen.fill((255,255,255))
    text_to_screen(screen, 'player {0} wins '.format(player), 300, square_size, Line_color)

image = pygame.image.load('src/tic.png' ).convert_alpha()
image = pygame.transform.scale(image, (Width, Height))

def start_screen():
    screen.fill((255,255,255))
    screen.blit(image,(0,0))
    playing = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playing == False:
                    xx = int(event.pos[0] // square_size)
                    yy = int(event.pos[1] // square_size)
                    playing == True
                    if (yy == 1 and xx == 1) or (yy == 0 and xx == 1):
                        reset()
                    elif (yy == 2 and xx == 0):
                        sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    playing = True
                    reset()
                elif event.key == pygame.K_r:
                    reset()
                    game_life = False
                elif event.key == pygame.K_q:
                    sys.exit()
            pygame.display.update()
    #text_to_screen(screen, 'Press P--> Play ', 300, square_size, Line_color)
    #text_to_screen(screen, ' Press Q--> Quit ', 600, 2*square_size, Line_color)

start_screen()



