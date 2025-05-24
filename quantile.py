import pandas as pd


def click_fun(win, Mlabel, df, name):
    q1 = df[name].quantile(0.25).round(2)
    q3 = df[name].quantile(0.75).round(2)
    Mlabel.config(text=f"1st quantile (25%): {q1} \n3rd quantile (75%): {q3} of {name}")
