def click_fun(win, Mlabel, df, name):
    count = df[name].count()
    Mlabel.config(text=f"Count of observations of {name}: {count}")
