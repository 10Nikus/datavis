import pandas as pd

df = pd.read_csv('data/sample_stock_data.csv')

print(f"Średnia arytmetyczna: {df['Volume'].mean()}")