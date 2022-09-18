from tkinter import *

root = Tk()

root.geometry('1200x800')
root.iconbitmap("D:\cpp\projectbase1\Paomedia-Small-N-Flat-Key.ico")
root.title("PASS SAVE")

label = Label()

button1 = Button(master=root, width="10", text="SAVE",
                 activebackground='red')

button1.place(x=50, y=50)
root.mainloop()
