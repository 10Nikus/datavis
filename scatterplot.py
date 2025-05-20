import matplotlib.pyplot as plt
import numpy as np

def click_fun(df, name):
    x = np.array(df['Date'])
    y = np.array(df[name])
    plt.scatter(x, y)
    plt.title(f"Plot of {name}")
    plt.xticks([])
    plt.tight_layout()
    plt.show()