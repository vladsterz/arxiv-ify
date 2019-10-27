from tkinter import *
import tkinter.ttk as ttk
if __name__ == "__main__":
    # s = ttk.Style()
    # s.theme_use('clam')
    root = Tk() 
    menu = Menu(root) 
    root.config(menu=menu) 
    filemenu = Menu(menu) 
    menu.add_cascade(label='File', menu=filemenu) 
    filemenu.add_command(label='New') 
    filemenu.add_command(label='Open...') 
    filemenu.add_separator() 
    filemenu.add_command(label='Exit', command=root.quit) 
    helpmenu = Menu(menu) 
    menu.add_cascade(label='Help', menu=helpmenu) 
    helpmenu.add_command(label='About') 
    mainloop() 