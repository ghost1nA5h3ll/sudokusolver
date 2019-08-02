board = [
    [0,3,0,0,7,0,9,0,0],
    [0,0,0,1,9,5,0,0,0],
    [0,0,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,0],
    [4,0,0,8,0,0,0,0,1],
    [0,0,0,0,2,0,0,0,0],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,0,0,0,7,0]
]

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
    for i in range(len(board[0])):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i,j)
    
    return None

def find_valid(board, number, pos):
    #x Achse (horizontal) BSP: board, 1 , (0,0)
    for i in range(len(board[pos[0]])):
        if number == board[pos[0]][i]:
            return False
    
    #y Achse (vertikale)
    for j in range(len(board[pos[0]])):
        if number == board[j][pos[1]]:
            return False

    #Box (3x3 Feld)
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_x * 3, box_x + 3):
        for j in range(box_y * 3, box_y + 3):
            if number == board[i][j]:
                return False
    
    return True


    

#print_sudoku(board)
valid = find_valid(board,5,(0,0))
print(valid)
