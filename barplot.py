import matplotlib.pyplot as plt
import numpy as np

def click_fun(df, name):
    x = np.array(df['Date'])
    y = np.array(df[name])
    plt.bar(x, y)
    plt.title(f"Plot of {name}")
    plt.xticks([])

    plt.ylim(bottom=min(y) * 0.9 , top=max(y) * 1.1)
    plt.show()