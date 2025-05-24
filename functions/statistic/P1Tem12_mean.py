def click_fun(win, Mlabel, df, name):
    mean_val = df[name].mean().round(2)
    Mlabel.config(text=f"Mean of {name}: {mean_val}")
