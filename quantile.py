import pandas as pd
from tkinter import messagebox

def click_fun(win, Mlabel):
    try:
        df = pd.read_csv('data/sample_stock_data.csv')
        quantile = df['Volume'].quantile(0.75)
        Mlabel.config(text=f"3rd quantile (75%): {quantile}")

    except FileNotFoundError:
        messagebox.showerror("Błąd", "Nie znaleziono pliku: data/sample_stock_data.csv")
    except Exception as e:
        messagebox.showerror("Błąd", f"Wystąpił problem: {e}")