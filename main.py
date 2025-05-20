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
from tkinter import messagebox, StringVar
from importer import import_csv

def assign_data():
  global data
  global name

  data = import_csv()
  if data is not None:
     if len(data.columns) > 1:
      name.set(data.columns[1])
     else:
      name.set(data.columns[0])
     print("zaimportowano dane")
       
zad = 1
import count as T01
print("Loading zad 1/", zad); zad += 1

import median as T02
print("Loading zad 2/", zad); zad += 1

import std as T03
print("Loading zad 3/", zad); zad += 1

import max_min as T04
print("Loading zad 4/", zad); zad += 1

import quantile as T05
print("Loading zad 5/", zad); zad += 1

import mean as T06
print("Loading zad 6/", zad); zad += 1

import bollinger as T07
print("Loading zad 7/", zad); zad += 1

import plot as T08
print("Loading zad 8/", zad); zad += 1

import scatterplot as T09
print("Loading zad 9/", zad); zad += 1

import barplot as T10
print("Loading zad 10/", zad); zad += 1

import histogram as T11
print("Loading zad 11/", zad); zad += 1

win = Tk()
name = StringVar()

def About():
  messagebox.showinfo('SuperSTAT', 'Program written by students of 2025 Python introductory class,\nver.: 2025/05/22.1')

def Quit(*event):
  quit()

def NoModule():
  messagebox.showinfo('ERROR', 'Module is improperly implemented, run directly')

def openTopLevel():
  top = Toplevel(win)
  top.title("Top Level Window")

  def setName(word):
    name.set(word)
    top.destroy()

  label = Label(top, text="Change data to be analyzed")
  label.pack(pady=20)
  columns = data.columns[1:]
  for col in columns:
    Button(top, text=col, command=lambda c=col: setName(c)).pack(pady=5)
  
  Button(top, text = "Exit", command = top.destroy).pack()

# options for buttons
grid_opt = {'padx' : 30, 'pady' : 5}

# Create a Label widget
Mlabel  = Label(win, text="[ Select module ]", font=('Arial', 14))
Mlabel.grid(row=0, columnspan=5)

MStatus = Label(win, text="...", font=('Arial', 14))
MStatus.grid(row=6, columnspan=5)
#Mlabel.pack(pady=40)

# Create commands buttons
ttk.Button(win, text="[  Count   ]", command=lambda: T01.click_fun(win, Mlabel, data, name.get())).grid(row=2, column=0, **grid_opt)
ttk.Button(win, text="[  Median   ]", command=lambda: T02.click_fun(win, Mlabel, data, name.get())).grid(row=2, column=1, **grid_opt)
ttk.Button(win, text="[  Std   ]", command=lambda: T03.click_fun(win, Mlabel, data, name.get())).grid(row=2, column=2, **grid_opt)
ttk.Button(win, text="[  Min Max   ]", command=lambda: T04.click_fun(win, Mlabel, data, name.get())).grid(row=2, column=3, **grid_opt)
ttk.Button(win, text="[  Quantile   ]", command=lambda: T05.click_fun(win, Mlabel, data, name.get())).grid(row=3, column=0, **grid_opt)
ttk.Button(win, text="[  Mean   ]", command=lambda: T06.click_fun(win, Mlabel, data, name.get())).grid(row=3, column=1, **grid_opt)
ttk.Button(win, text="[  Bollinger   ]", command=lambda: T07.click_fun(win, Mlabel, data, name.get())).grid(row=3, column=2, **grid_opt)
ttk.Button(win, text="[  Plot   ]", command=lambda: T08.click_fun(data, name.get())).grid(row=1, column=0, **grid_opt)
ttk.Button(win, text="[  Scatterplot   ]", command=lambda: T09.click_fun(data, name.get())).grid(row=1, column=1, **grid_opt)
ttk.Button(win, text="[  Barplot   ]", command=lambda: T10.click_fun(data, name.get())).grid(row=1, column=2, **grid_opt)
ttk.Button(win, text="[  Histogram   ]", command=lambda: T11.click_fun(data, name.get())).grid(row=1, column=3, **grid_opt)

#=====================
ttk.Button(win, text="[ About the program: ]", command=About).grid(row=5,column=2, columnspan = 1 )
ttk.Button(win, text="[ Close   ]", command=Quit).grid(row=5, column=3, columnspan = 1)
ttk.Button(win, text="[ Import CSV ]", command=assign_data).grid(row=5, column=0, columnspan=1)
ttk.Button(win, text="[ Change Data ]", command=openTopLevel).grid(row=3, column=3, columnspan=1)

win.bind("<KeyPress-Escape>", Quit)
win.protocol("WM_DELETE_WINDOW", Quit)

# start interface:
assign_data()
win.mainloop()