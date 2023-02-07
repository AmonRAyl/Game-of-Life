import random
import sys
import pygame
import copy

SCREEN_WIDTH = 1001
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

    # Glider
    # board[10][10].setState(green)
    # board[10][10].setValue(1)

    # board[11][11].setState(green)
    # board[11][11].setValue(1)

    # board[11][12].setState(green)
    # board[11][12].setValue(1)

    # board[9][12].setState(green)
    # board[9][12].setValue(1)

    # board[10][12].setState(green)
    # board[10][12].setValue(1)

    # Random
    for i in range(boardSize):
        for j in range(boardSize):
            if(random.randint(0, 1) == 1):
                board[i][j].setState(green)
                board[i][j].setValue(1)
    return board, screen


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


def main():
 # User input number of iterations
    board, screen = init()
    for i in range(0, 50):
        for j in range(0, 50):
            pygame.draw.rect(screen, board[i][j].getState(), pygame.Rect(
                board[i][j].getX(), board[i][j].getY(), 19, 19))
    pygame.display.flip()
    while True:
        # Posibles entradas del teclado y mouse
        alt_board = copy.deepcopy(board)
        board = check_cells(board)
        for i in range(0, 50):
            for j in range(0, 50):
                if alt_board[i][j].getState() != board[i][j].getState():
                    pygame.draw.rect(screen, board[i][j].getState(), pygame.Rect(
                        board[i][j].getX(), board[i][j].getY(), 19, 19))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


main()
