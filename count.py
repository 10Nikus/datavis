import pandas as pd
from tkinter import messagebox


def click_fun(win, Mlabel, df, name):
    try:
        count = df[name].count()
        Mlabel.config(text=f"Count of observations of {name}: {count}")
        
    except FileNotFoundError:
        messagebox.showerror("Błąd", "Nie znaleziono pliku: data/sample_stock_data.csv")
 
    except Exception as e:
        messagebox.showerror("Błąd", f"Wystąpił problem: {e}")
