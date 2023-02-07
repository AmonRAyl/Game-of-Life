import random
import sys
import pygame
import copy

SCREEN_WIDTH = 1068
SCREEN_HEIGHT = 1001


class Cell:
    def __init__(self, x, y, state, value):
        self.x = x
        self.y = y
        self.state = state
        self.value = value

    def setState(self, state):
        self.state = state

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def getState(self):
        return self.state

    def getX(self):
        return self.x

    def getY(self):
        return self.y


def init():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Game of Life")

    fondo = pygame.image.load("Board1001.png").convert()
    screen.blit(fondo, (0, 0))

    white = (255, 255, 255)
    green = (0, 255, 0)

    boardSize = 50
    board = [[Cell(1+20*i, 1+20*j, white, 0)
              for i in range(boardSize)] for j in range(boardSize)]
    
    #Play Pause buttons
    font = pygame.font.SysFont("Arial", 30)
    
    text = font.render("Play", 1, ( 69, 49, 7 ))
    text2 = font.render("Pause", 1, ( 69, 49, 7 ))
    text3 = font.render("Clear", 1, ( 69, 49, 7 ))
    
    x, y, w , h = text.get_rect()
    x, y, w2 , h2 = text2.get_rect()
    x, y, w3 , h3 = text3.get_rect()
    
    pygame.draw.rect(screen, (  233, 169, 36 ), (1000, 0, 68 , h))
    playButton=screen.blit(text,  (1000, 0)) 
    
    pygame.draw.rect(screen, (  233, 169, 36 ), (1000, h+1, 68 , h2))
    pauseButton=screen.blit(text2,  (1000, h)) 
    
    pygame.draw.rect(screen, (  233, 169, 36 ), (1000, h+h2+2, 68 , h3))
    clearButton=screen.blit(text3,  (1000, h2+h)) 
    
    pygame.display.flip() 
    
    return board, screen,playButton,pauseButton,clearButton


def check_cells(board):
    new_board = copy.deepcopy(board)
    for i in range(0, 50):
        for j in range(0, 50):
            value, color = check_dead_or_alive(board, i, j)
            new_board[i][j].setValue(value)
            new_board[i][j].setState(color)
    board = copy.deepcopy(new_board)
    return board


def check_dead_or_alive(board, x, y):
    count = 0
    # check boundaries of board[x][y] and sum its values
    if x-1 >= 0 and y-1 >= 0:
        count += board[x-1][y-1].getValue()  # top left corner
    if x-1 >= 0:
        count += board[x-1][y].getValue()  # top
    if x-1 >= 0 and y+1 <= 49:
        count += board[x-1][y+1].getValue()  # top right corner
    if y-1 >= 0:
        count += board[x][y-1].getValue()  # left
    if y+1 <= 49:
        count += board[x][y+1].getValue()  # right
    if x+1 <= 49 and y-1 >= 0:
        count += board[x+1][y-1].getValue()  # bottom left corner
    if x+1 <= 49:
        count += board[x+1][y].getValue()  # bottom
    if x+1 <= 49 and y+1 <= 49:
        count += board[x+1][y+1].getValue()  # bottom right corner
    # check if cell is dead or alive
    if board[x][y].getValue() == 0 and count == 3:
        return 1, (0, 255, 0)
    if board[x][y].getValue() == 1 and (count == 2 or count == 3):
        return 1, (0, 255, 0)
    return 0, (255, 255, 255)

def boardDisplay(board,screen): 
    for i in range(0, 50):
        for j in range(0, 50):
            pygame.draw.rect(screen, board[i][j].getState(), pygame.Rect(
                board[i][j].getX(), board[i][j].getY(), 19, 19))
    pygame.display.flip()

def main():
 # User input number of iterations
    board, screen,playButton,pauseButton,clearButton = init()
    boardDisplay(board,screen)
    
    play=False
    
    while True:
        mousex, mousey = pygame.mouse.get_pos()
        mousex=int(mousex/20)
        mousey=int(mousey/20)
        # Posibles entradas del teclado y mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
             sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if playButton.collidepoint(event.pos):
                    play=True
                if pauseButton.collidepoint(event.pos):
                    play=False
                if clearButton.collidepoint(event.pos):
                    play=False
                    board, screen, = init()[0:2]
                if mousex <50 and mousex>=0 and mousey <50 and mousey>=0:
                    if board[mousey][mousex].getValue()==1:
                        board[mousey][mousex].setState((255, 255, 255))
                        board[mousey][mousex].setValue(0)
                    else:
                        board[mousey][mousex].setState((0, 255, 0))
                        board[mousey][mousex].setValue(1)
                    boardDisplay(board,screen)
        if(play==True):
            alt_board = copy.deepcopy(board)
            board = check_cells(board)
            boardDisplay(board,screen)
        pygame.display.flip()
       
main()