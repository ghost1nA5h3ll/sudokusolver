import sudoku
import tkinter
import PIL

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
root = tkinter.Tk()

menu = tkinter.Menu(root)
root.config(menu= menu)

filemenu = tkinter.Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New",command=lambda: sudoku.generate_sudoku(50))

root.geometry("800x800")

sudoku.print_sudoku(board)

root.mainloop()
