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
from functions.importer import import_csv
import functions.statistic.count as count
import functions.statistic.median as median 
import functions.statistic.std as std 
import functions.statistic.max_min as max_min 
import functions.statistic.quantile as quantile 
import functions.statistic.mean as mean 
import functions.bollinger 
import functions.plots.plot as plot 
import functions.plots.scatterplot as scatterplot 
import functions.plots.barplot as barplot 
import functions.plots.histogram as histogram 

def assign_data():
  global data
  global name

  data, filepath = import_csv()

  print(f"zaimportowano dane z {filepath}")
  
  if data is not None:
     for widget in button_box.winfo_children():
      if isinstance(widget, ttk.Button):
        widget.config(state="normal")
     MStatus.config(text=f"[ Data loaded: {filepath} ]")
     Mlabel.config(text=f"[Select module]")
     state = "normal"
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
  top.title("Select Data Column")
  top.geometry("300x300")
  top.resizable(width=False, height=False)
  wrapper = Frame(top, padx=20, pady=20)
  wrapper.pack(expand=True, fill=BOTH)
  def setName(word):
    name.set(word)
    top.destroy()

  columns = data.columns[1:]
  for col in columns:
    ttk.Button(wrapper, text=col, width=12, command=lambda c=col: setName(c)).pack(pady=5)
  
  ttk.Button(top, text = "Exit", command = top.destroy).pack()




win = Tk()
win.geometry("600x250")
win.title("Data Analysis and Visualization Tool")
win.resizable(width=False, height=False)

name = StringVar()
grid_opt = {'padx' : 30, 'pady' : 5}


Mlabel  = Label(win, height=3, text="[ Please load data first ]", font=('Arial', 14))
Mlabel.pack(pady=5)

outer = Frame(win)
outer.pack(expand=True)

button_box = Frame(outer)
button_box.pack()
MStatus = Label(win, text='', font=('Arial', 7))
MStatus.pack(pady=2)

ttk.Button(button_box, text="Count", width=12, state="disabled", command=lambda: count.click_fun(win, Mlabel, data, name.get())).grid(row=2, column=0, **grid_opt)
ttk.Button(button_box, text="Median", width=12 , state="disabled", command=lambda: median.click_fun(win, Mlabel, data, name.get())).grid(row=2, column=1, **grid_opt)
ttk.Button(button_box, text="Std", width=12 , state="disabled", command=lambda: std.click_fun(win, Mlabel, data, name.get())).grid(row=2, column=2, **grid_opt)
ttk.Button(button_box, text="Min Max", width=12 , state="disabled", command=lambda: max_min.click_fun(win, Mlabel, data, name.get())).grid(row=2, column=3, **grid_opt)
ttk.Button(button_box, text="Quantile", width=12 , state="disabled", command=lambda: quantile.click_fun(win, Mlabel, data, name.get())).grid(row=3, column=0, **grid_opt)
ttk.Button(button_box, text="Mean", width=12 , state="disabled", command=lambda: mean.click_fun(win, Mlabel, data, name.get())).grid(row=3, column=1, **grid_opt)
ttk.Button(button_box, text="Bollinger", width=12 , state="disabled", command=lambda: bollinger.click_fun(win, Mlabel, data, name.get())).grid(row=3, column=2, **grid_opt)
ttk.Button(button_box, text="Plot", width=12 , state="disabled", command=lambda: plot.click_fun(data, name.get())).grid(row=1, column=0, **grid_opt)
ttk.Button(button_box, text="Scatterplot", width=12 , state="disabled", command=lambda: scatterplot.click_fun(data, name.get())).grid(row=1, column=1, **grid_opt)
ttk.Button(button_box, text="Barplot", width=12 , state="disabled", command=lambda: barplot.click_fun(data, name.get())).grid(row=1, column=2, **grid_opt)
ttk.Button(button_box, text="Histogram", width=12 , state="disabled", command=lambda: histogram.click_fun(data, name.get())).grid(row=1, column=3, **grid_opt)

ttk.Button(button_box, text="Close", width=12,  command=Quit).grid(row=5, column=3, columnspan = 1, **grid_opt)
ttk.Button(button_box, text="Load data", width=12,  command=assign_data).grid(row=5, column=0, columnspan=1, **grid_opt)
ttk.Button(button_box, text="Change Data", width=12, state="disabled",  command=openTopLevel).grid(row=3, column=3, columnspan=1, **grid_opt)

win.bind("<KeyPress-Escape>", Quit)
win.protocol("WM_DELETE_WINDOW", Quit)


win.mainloop()