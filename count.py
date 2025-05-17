import pandas as pd
from tkinter import messagebox

def click_fun(win, Mlabel):
    try:
        df = pd.read_csv('data/sample_stock_data.csv')
        count = df['Volume'].count()
        Mlabel.config(text=f"[ count ] Liczba obserwacji: {count}")
        print(f"Liczba obserwacji: {count}")
    except FileNotFoundError:
        messagebox.showerror("Błąd", "Nie znaleziono pliku: data/sample_stock_data.csv")
    except Exception as e:
        messagebox.showerror("Błąd", f"Wystąpił problem: {e}")
