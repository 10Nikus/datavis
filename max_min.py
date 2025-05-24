def click_fun(win, Mlabel, df, name):
    min_val = df[name].min().round(3)
    max_val = df[name].max().round(3)
    Mlabel.config(text=f"Minimum: {min_val} \nMaximum: {max_val} of {name}")
