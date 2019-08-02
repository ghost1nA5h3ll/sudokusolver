import sudoku
import tkinter
import PIL

board = sudoku.generate_sudoku(69)

def renew_board(number):
    board = sudoku.generate_sudoku(number)
    sudoku.print_sudoku(board)

root = tkinter.Tk()
root.geometry("800x800")

main_frame = tkinter.Frame(root,bg='blue')
btn_frame = tkinter.Frame (root,bg = 'red')

solve_button = tkinter.Button(btn_frame,text='Solve Game')
check_button = tkinter.Button(btn_frame,text='Check Game')
renew_button = tkinter.Button(btn_frame,text='New Game', command=lambda: renew_board(69))


sudoku.print_sudoku(board)

#place all components
main_frame.place(relx=0.1,rely=0.1,relheight=0.7,relwidth=0.8)
btn_frame.place(relx=0.1,rely=0.81,relheight=0.15,relwidth=0.8)
solve_button.place(relx=0.03,rely=0.1,relheight= 0.8,relwidth=0.3)
check_button.place(relx=0.35,rely=0.1,relheight=0.8,relwidth=0.3)
renew_button.place(relx=0.67,rely=0.1,relheight=0.8,relwidth=0.3)

root.mainloop()
