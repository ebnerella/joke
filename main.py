from tkinter import *
from  tkinter import messagebox
import random
def no():
    messagebox.showinfo('', 'GOTCHA')
    quit()
def motionMouse(event):
    btn.place(x=random.randint(100, 500), y=random.randint(100, 300))
root = Tk()
root.geometry('600x400')
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.wm_geometry("+%d+%d" % (x, y))
root.title('')
root.resizable(width=False, height=False)
root['bg'] = 'white'
label = Label(root, text='Ты даун?', font='Arial 18 bold', bg='white').pack()
btn = Button(root, text='Нет', font='Arial 18 bold')
btn.place(x=170, y=100)
btn.bind('<Enter>', motionMouse)
bttn = Button(root, text='Да', font='Arial 18 bold', command=no).place(x=350, y=100)
root.mainloop()
