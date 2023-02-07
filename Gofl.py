import random
import copy
import time

def init():
    boardSize = 10
    board = [[0 for i in range(boardSize)] for j in range(boardSize)] 
    board[5][5]=1
    board[6][6]=1
    board[6][7]=1
    board[5][7]=1
    board[4][7]=1

    #for i in range(boardSize):
    #    for j in range(boardSize):
    #        board[i][j] = random.randint(0,1)
    return board

def check_cells(board):
    new_board= copy.deepcopy(board)
    for i in range(0,10):
        for j in range(0,10):
            new_board[i][j]=check_dead_or_alive(board,i,j)
    board=copy.deepcopy(new_board)
    return board

def check_dead_or_alive(board,x,y):
    count=0
    #check boundaries of board[x][y] and sum its values
    if x-1>=0 and y-1>=0:
        count+=board[x-1][y-1] #top left corner
    if x-1>=0: 
        count+=board[x-1][y] #top
    if x-1>=0 and y+1<=9:
        count+=board[x-1][y+1] #top right corner
    if y-1>=0: 
        count+=board[x][y-1] #left
    if y+1<=9:
        count+=board[x][y+1] #right
    if x+1<=9 and y-1>=0:
        count+=board[x+1][y-1] #bottom left corner
    if x+1<=9: 
        count+=board[x+1][y] #bottom
    if x+1<=9 and y+1<=9: 
        count+=board[x+1][y+1] #bottom right corner
    #check if cell is dead or alive
    if board[x][y] == 0 and count == 3:
        return 1
    if board[x][y] == 1 and (count == 2 or count == 3):
        return 1
    return 0

def main():
 #User input number of iterations
    iterations = int(input("Enter number of iterations: "))
    board = init()
    for i in range(iterations):
        print("Iteration: ", i)
        board=check_cells(board)
        for row in board:
            print(row)
        time.sleep(1)

main()