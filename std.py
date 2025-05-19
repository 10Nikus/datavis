import pandas as pd
from tkinter import messagebox

def click_fun(win, Mlabel, df):
    try:
        
        std = df['Volume'].std()
        Mlabel.config(text=f"Standard deviation: {std}")
        
    except FileNotFoundError:
        messagebox.showerror("Błąd", "Nie znaleziono pliku: data/sample_stock_data.csv")
    except Exception as e:
        messagebox.showerror("Błąd", f"Wystąpił problem: {e}")