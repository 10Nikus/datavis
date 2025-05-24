import matplotlib.pyplot as plt

def click_fun(win, label, data, column_name):
    prices = data[column_name].astype(float)
    sma = prices.rolling(20).mean()
    std = prices.rolling(20).std()

    upper = sma + 2 * std
    lower = sma - 2 * std

    plt.plot(prices, label='Price')
    plt.plot(sma, label='SMA (20)')
    plt.plot(upper, label='Upper Band')
    plt.plot(lower, label='Lower Band')
    plt.legend()
    plt.title(f'Bollinger Bands of {column_name}')
    plt.grid()
    plt.show()

