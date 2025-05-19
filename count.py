import pandas as pd
from tkinter import messagebox

def click_fun(win, Mlabel, df):
    try:
        df = pd.read_csv('data/sample_stock_data.csv')
        count = df['Volume'].count()
        Mlabel.config(text=f"Count of observations: {count}")
        
    except FileNotFoundError:
        messagebox.showerror("Błąd", "Nie znaleziono pliku: data/sample_stock_data.csv")
    except Exception as e:
        messagebox.showerror("Błąd", f"Wystąpił problem: {e}")
