import pandas as pd
from tkinter import messagebox

def click_fun(win, Mlabel):
    try:
        df = pd.read_csv('data/sample_stock_data.csv')
        min = df['Volume'].min()
        max = df['Volume'].max()
        Mlabel.config(text=f"Minimum: {min} \nMaximum: {max}")

    except FileNotFoundError:
        messagebox.showerror("Błąd", "Nie znaleziono pliku: data/sample_stock_data.csv")
    except Exception as e:
        messagebox.showerror("Błąd", f"Wystąpił problem: {e}")