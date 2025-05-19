import pandas as pd
from tkinter import messagebox
from importer import assign_data

def click_fun(win, Mlabel, df, name):
    try:
        
        std = df[name].std()
        Mlabel.config(text=f"Standard deviation of {name}: {std}")
        
    except FileNotFoundError:
        messagebox.showerror("Błąd", "Nie znaleziono pliku. Zaimportuj plik")
        
    except Exception as e:
        messagebox.showerror("Błąd", f"Wystąpił problem: {e}")