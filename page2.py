from tkinter import *

from PIL import ImageTk


ws = Tk()
ws.geometry('400x300')
ws.title('WELCOME')

f = ("Times bold", 14)
 
def start():
    ws.destroy()
    import page3

def Exit():
    ws.destroy()
    for i in range(5):
        if i == 3:
            break

def option():
    ws.destroy()
    import page1

Label(
    ws,
    text="WELCOME TO GAME",
    padx=50,
    pady=50,
    font=f,

).pack(expand=True, fill=BOTH)

Button(
    ws, 
    text="Start Game", 
    font=f,
    command=start
    ).pack(fill=X, expand=TRUE, side=LEFT)
Button(
    ws,
    text="Rules",
    font=f,
    command=option
    ).pack(fill=X, expand=TRUE, side=LEFT)
Button(
    ws, 
    text="Exit", 
    font=f,
    command=Exit
    ).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()
