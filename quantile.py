import pandas as pd
from tkinter import messagebox


def click_fun(win, Mlabel, df, name):
    try:
        quantile1 = df[name].quantile(0.25)
        quantile3 = df[name].quantile(0.75)
        Mlabel.config(text=f"1rd quantile (25%): {quantile1} \n 3rd quantile (75%): {quantile3} of {name}")

    except FileNotFoundError:
        messagebox.showerror("Błąd", "Nie znaleziono pliku: data/sample_stock_data.csv")

    except Exception as e:
        messagebox.showerror("Błąd", f"Wystąpił problem: {e}")