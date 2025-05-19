import pandas as pd
from tkinter import messagebox

def click_fun(win, Mlabel, df, name):
    try:

        median = df[name].median()
        Mlabel.config(text=f"Median of {name}: {median}")

    except FileNotFoundError:
        messagebox.showerror("Błąd", "Nie znaleziono pliku: data/sample_stock_data.csv")

    except Exception as e:
        messagebox.showerror("Błąd", f"Wystąpił problem: {e}")