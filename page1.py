from tkinter import *
def Main():
    ws.destroy()
    import page2

ws = Tk()
ws.geometry('600x600')
ws.title('RULES')
Label(ws, text='Rules To Play :', font=("Times New Roman", 30)).place(x=160, y=30)
Label(ws, text='Rock wins against scissors', font=("Times New Roman", 25)).place(x=130, y=100)
Label(ws, text='Scissors win against paper', font=("Times New Roman", 25)).place(x=130, y=150)
Label(ws, text='Paper wins against rock', font=("Times New Roman", 25)).place(x=130, y=200)
Label(ws, text='Stick win against Scissors', font=("Times New Roman", 25)).place(x=130, y=250)
Label(ws, text='Paper wins against Stick', font=("Times New Roman", 25)).place(x=130, y=300)
Label(ws, text='Rock wins against Stick', font=("Times New Roman", 25)).place(x=130, y=350)

Label(ws, text='Wait for 3 seconds for AI move', font=("Times New Roman", 25)).place(x=90, y=400)

Label(ws, text='which player get 5 points get win', font=("Times New Roman", 25)).place(x=90, y=450)
Button(ws, text="Back To Main Menu", font=("Times New Roman", 15), command=Main).place(x=200, y=520)
ws.mainloop()
