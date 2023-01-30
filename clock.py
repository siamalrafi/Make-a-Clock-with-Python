from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title('Clock')

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)


label = Label(root, font=(), background="black", foreground="cyan")
label.pack(anchor='center')
time()

# clock making
mainloop()
print('this is clock')
