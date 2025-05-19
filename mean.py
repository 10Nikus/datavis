import pandas as pd
from tkinter import messagebox

def click_fun(win, Mlabel,df):
    try:
        
        mean = df['Volume'].mean()
        Mlabel.config(text=f"Mean: {mean}")
        
    except FileNotFoundError:
        messagebox.showerror("Błąd", "Nie znaleziono pliku: data/sample_stock_data.csv")
    except Exception as e:
        messagebox.showerror("Błąd", f"Wystąpił problem: {e}")