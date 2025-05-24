import pandas as pd

def click_fun(win, Mlabel, df, name):
    std_val = df[name].std().round(2)
    Mlabel.config(text=f"Standard deviation of {name}: {std_val}")
