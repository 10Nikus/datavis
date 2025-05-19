"""
  interaktywna aplikacja do analizy i wizualizacji danych giełdowych z wykorzystaniem wskaźników technicznych 
  i statystyk opisowych, zawierająca:
    1) import danych z pliku CSV
    2) statystyki opisowe
    3) interaktywną wizualizację danych (wykres/y)
    4) wskaźniki Bollingera 
"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from importer import assign_data

global data
global name




zad = 1
print("Loading zad 1/", zad); zad += 1
import count as T01

print("Loading zad 2/", zad); zad += 1
import median as T02

print("Loading zad 3/", zad); zad += 1
import std as T03

print("Loading zad 4/", zad); zad += 1
import max_min as T04

print("Loading zad 5/", zad); zad += 1
import quantile as T05

print("Loading zad 6/", zad); zad += 1
import mean as T06

print("Loading zad 6/", zad); zad += 1
#import bollinger as T06

win = Tk()
# win.geometry("400x200")
# win.minsize(400,200)
# # win.maxsize(400,200)

def About():
  messagebox.showinfo('SuperSTAT', 'Program written by students of 2025 Python introductory class,\nver.: 2025/03/22.1')

def Quit(*event):
  quit()

def NoModule():
  messagebox.showinfo('ERROR', 'Module is improperly implemented, run directly')

# options for buttons
## for pack: button_opt = {'fill': constants.BOTH, 'padx': 15, 'pady': 5}
grid_opt = {'padx' : 30, 'pady' : 5}

# Create a Label widget
Mlabel  = Label(win, text="[ Select module ]", font=('Arial', 14))
Mlabel.grid(row=0, columnspan=5)

MStatus = Label(win, text="...", font=('Arial', 14))
MStatus.grid(row=5, columnspan=5)
#Mlabel.pack(pady=40)


# Create commands buttons

ttk.Button(win, text="[  count   ]", command=lambda: T01.click_fun(win, Mlabel, data, name)).grid(row=1, column=0, **grid_opt)
ttk.Button(win, text="[  median   ]", command=lambda: T02.click_fun(win, Mlabel, data, name)).grid(row=1, column=1, **grid_opt)
ttk.Button(win, text="[  std   ]", command=lambda: T03.click_fun(win, Mlabel, data, name)).grid(row=1, column=2, **grid_opt)
ttk.Button(win, text="[  min max   ]", command=lambda: T04.click_fun(win, Mlabel, data, name)).grid(row=2, column=0, **grid_opt)
ttk.Button(win, text="[  quantile   ]", command=lambda: T05.click_fun(win, Mlabel, data, name)).grid(row=2, column=1, **grid_opt)
ttk.Button(win, text="[  mean   ]", command=lambda: T06.click_fun(win, Mlabel, data, name)).grid(row=2, column=2, **grid_opt)
ttk.Button(win, text="[  bollinger   ]", command=lambda: T07.click_fun(win, Mlabel, data, name)).grid(row=3, column=0, **grid_opt)
ttk.Button(win, text="[  costam   ]", command=lambda: T07.click_fun(win, Mlabel, data, name)).grid(row=3, column=1, **grid_opt)
ttk.Button(win, text="[  costam   ]", command=lambda: T07.click_fun(win, Mlabel, data, name)).grid(row=3, column=2, **grid_opt)


#=====================
ttk.Button(win, text="[ O programie: ]", command=About).grid(row=4,column=0, columnspan = 1 )
ttk.Button(win, text="[    Zamknij   ]", command=Quit).grid(row=4, column=1, columnspan = 1)
ttk.Button(win, text="[ Import CSV ]", command=assign_data).grid(row=4, column=2, columnspan=1)



win.bind("<KeyPress-Escape>", Quit)
win.protocol("WM_DELETE_WINDOW", Quit)
# start interface:
win.mainloop()
## print(f"(Main)data = {data}") # global variable data is known to all madules
