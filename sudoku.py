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
            

print_sudoku(board)