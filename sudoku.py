#import the needed modules
import random

#generates a sudoku and hides given amount of numbers
def generate_sudoku(board,number):
    #filling the empty board with random numbers from 0 to 9
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] = random.randint(0,9)
    #try to solve the given random board
    if solve_sudoku(board):
        #it's solveable -> hiding given amount of numbers
        for x in range(0,number):
            rnd_x = random.randint(0,8)
            rnd_y = random.randint(0,8)

            if board[rnd_y][rnd_x] != 0:
                board[rnd_y][rnd_x] = 0
        return board
    else:
        #board is not solveable so just start again
        return generate_sudoku(board,number)

#printing a given board
def print_sudoku(board):
    # i is the Y direction and j is X direction
    for i in range(len(board[0])):
        if i % 3 == 0 and i != 0:            
            print("- - - - - - - -")
        for j in range(len(board[i])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j != 8:
                print(board[i][j],end="")
            else:
                print(board[i][j])
            
#finds the first empty field in a given board and return tuple of "cordinates"

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

    #no free field was found
    return None

#validates the given number at given position in a given board
def find_valid(board, number, pos):
    #x direction 
    for i in range(len(board[0])):
        if number == board[pos[0]][i] and pos[1] != i:
            return False
    
    #y direction
    for j in range(len(board)):
        if number == board[j][pos[1]] and pos[0] != j:
            return False

    #Box (3x3 field)
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if number == board[i][j] and (i,j) != pos:
                return False
    
    return True

#solves the given sudoku and return True. If not solveable it's returning False
def solve_sudoku(board):
    #finds the first free position
    pos = find_empty(board)
    if not pos:
        return True #all fields are filled
    else:
        row, col = pos #free position is initialized

    for i in range(1,10):
        if find_valid(board, i, (row, col)):
            board[row][col] = i #Setting the field to value of "i" if it's valid
            
            if solve_sudoku(board):
                return True #It's solved
        
            board[row][col] = 0 #backtracking and setting the field to 0
    return False #Not solveable