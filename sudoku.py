import random

""" board = [
    [0, 3, 0, 0, 7, 0, 9, 0, 0],
    [0, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 0, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 0],
    [4, 0, 0, 8, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 0, 0, 0, 7, 0]
] """

def generate_sudoku(number):
    board = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,6,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ]
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] = random.randint(0,9)

    if solve_sudoku(board):
        for x in range(0,number):
            rnd_x = random.randint(0,8)
            rnd_y = random.randint(0,8)

            if board[rnd_y][rnd_x] != 0:
                board[rnd_y][rnd_x] = 0
        return board
    else:
        return generate_sudoku(number)


def print_sudoku(board):
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
            

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    
    return None

def find_valid(board, number, pos):
    #x Achse (horizontal) BSP: board, 1 , (0,0)
    for i in range(len(board[0])):
        if number == board[pos[0]][i] and pos[1] != i:
            return False
    
    #y Achse (vertikale)
    for j in range(len(board)):
        if number == board[j][pos[1]] and pos[0] != j:
            return False

    #Box (3x3 Feld)
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if number == board[i][j] and (i,j) != pos:
                return False
    
    return True

def solve_sudoku(board):
    pos = find_empty(board)
    if not pos:
        return True
    else:
        row, col = pos

    for i in range(1,10):
        if find_valid(board, i, (row, col)):
            board[row][col] = i
            
            if solve_sudoku(board):
                return True
        
            board[row][col] = 0
    return False

board  = generate_sudoku(61)
print_sudoku(board)