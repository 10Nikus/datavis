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

def assign_data():
  global data
  global name

  data, filepath = import_csv()

  print(f"zaimportowano dane z {filepath}")
  MStatus.config(text=f"[ Data loaded: {filepath} ]")
  if data is not None:
     if len(data.columns) > 1:
      name.set(data.columns[1])
     else:
      name.set(data.columns[0])
  
     print("zaimportowano dane")

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


win = Tk()
win.geometry("600x250")
win.title("Data Analysis and Visualization Tool")
win.resizable(width=False, height=False)

name = StringVar()
grid_opt = {'padx' : 30, 'pady' : 5}

# Create a Label widget
Mlabel  = Label(win, text="[ Select module ]", font=('Arial', 14))
Mlabel.pack(pady=5)

MStatus = Label(win, text='Please load data', font=('Arial', 14))
MStatus.pack(pady=2)

outer = Frame(win)
outer.pack(expand=True)

button_box = Frame(outer)
button_box.pack()

# Create commands buttons
ttk.Button(button_box, text="Count", width=12, command=lambda: T01.click_fun(win, Mlabel, data, name.get())).grid(row=2, column=0, **grid_opt)
ttk.Button(button_box, text="Median", width=12, command=lambda: T02.click_fun(win, Mlabel, data, name.get())).grid(row=2, column=1, **grid_opt)
ttk.Button(button_box, text="Std", width=12, command=lambda: T03.click_fun(win, Mlabel, data, name.get())).grid(row=2, column=2, **grid_opt)
ttk.Button(button_box, text="Min Max", width=12, command=lambda: T04.click_fun(win, Mlabel, data, name.get())).grid(row=2, column=3, **grid_opt)
ttk.Button(button_box, text="Quantile", width=12, command=lambda: T05.click_fun(win, Mlabel, data, name.get())).grid(row=3, column=0, **grid_opt)
ttk.Button(button_box, text="Mean", width=12, command=lambda: T06.click_fun(win, Mlabel, data, name.get())).grid(row=3, column=1, **grid_opt)
ttk.Button(button_box, text="Bollinger", width=12, command=lambda: T07.click_fun(win, Mlabel, data, name.get())).grid(row=3, column=2, **grid_opt)
ttk.Button(button_box, text="Plot", width=12, command=lambda: T08.click_fun(data, name.get())).grid(row=1, column=0, **grid_opt)
ttk.Button(button_box, text="Scatterplot", width=12, command=lambda: T09.click_fun(data, name.get())).grid(row=1, column=1, **grid_opt)
ttk.Button(button_box, text="Barplot", width=12, command=lambda: T10.click_fun(data, name.get())).grid(row=1, column=2, **grid_opt)
ttk.Button(button_box, text="Histogram", width=12, command=lambda: T11.click_fun(data, name.get())).grid(row=1, column=3, **grid_opt)

ttk.Button(button_box, text="Close", width=12, command=Quit).grid(row=5, column=3, columnspan = 1, **grid_opt)
ttk.Button(button_box, text="Import CSV", width=12, command=assign_data).grid(row=5, column=0, columnspan=1, **grid_opt)
ttk.Button(button_box, text="Change Data", width=12, command=openTopLevel).grid(row=3, column=3, columnspan=1, **grid_opt)

win.bind("<KeyPress-Escape>", Quit)
win.protocol("WM_DELETE_WINDOW", Quit)

# start interface:

win.mainloop()