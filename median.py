import pandas as pd

def click_fun(win, Mlabel, df, name):
    median_val = df[name].median().round(2)
    Mlabel.config(text=f"Median of {name}: {median_val}")
