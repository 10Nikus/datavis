import matplotlib.pyplot as plt
import numpy as np

def click_fun(df, name):
    y = np.array(df[name])
    plt.plot(y, '-g')
    plt.title(f"Plot of {name}")
    plt.xticks([])
    plt.show()