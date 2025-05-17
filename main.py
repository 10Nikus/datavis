import pandas as pd

'''  interaktywna aplikacja do analizy i wizualizacji danych giełdowych z wykorzystaniem wskaźników technicznych i statystyk opisowych, zawierająca:
1) import danych z pliku CSV
2) statystyki opisowe
3) interaktywną wizualizację danych (wykres/y)
4) wskaźniki Bollingera '''

df = pd.read_csv('data/sample_stock_data.csv')

print(df["Volume"].median())

