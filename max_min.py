import pandas as pd
from tkinter import messagebox


def click_fun(win, Mlabel, df, name):
    try:
        min = df[name].min()
        max = df[name].max()
        Mlabel.config(text=f"Minimum: {min} \nMaximum: {max} of {name}")

    except FileNotFoundError:
        messagebox.showerror("Błąd", "Nie znaleziono pliku: data/sample_stock_data.csv")

    except Exception as e:
        messagebox.showerror("Błąd", f"Wystąpił problem: {e}")