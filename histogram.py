import matplotlib.pyplot as plt
import numpy as np

def click_fun(df, name):
    y = np.array(df[name])
    plt.hist(y)
    plt.title(f"Histogram of {name}")
    plt.show()