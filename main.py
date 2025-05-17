import pandas as pd
import matplotlib.pyplot as plt

'''  
    interaktywna aplikacja do analizy i wizualizacji danych giełdowych z wykorzystaniem wskaźników technicznych i statystyk opisowych, zawierająca:
    1) import danych z pliku CSV
    2) statystyki opisowe
    3) interaktywną wizualizację danych (wykres/y)
    4) wskaźniki Bollingera 
'''

df = pd.read_csv('data/sample_stock_data.csv')

print("Statystyki opisowe: ")
print(df.describe())

print(f"Liczba obserwacji: {df['Volume'].count()}")
print(f"Mediana: {df['Volume'].median()}")
print(f"Odchylenie standardowe: {df['Volume'].std()}")
print(f"Wartość minimalna: {df['Volume'].min()}")
print(f"Wartość maksymalna: {df['Volume'].max()}")
print(f"3 kwartyl (75%): {df['Volume'].quantile(0.75)}")

# wskazniki bollingera
df['SMA20'] = df['Close'].rolling(window=20).mean()
df['UpperBand'] = df['SMA20'] + 2 * df['Close'].rolling(window=20).std()
df['LowerBand'] = df['SMA20'] - 2 * df['Close'].rolling(window=20).std()

plt.figure(figsize=(14, 6))
plt.plot(df['Date'], df['Close'], label='Cena zamknięcia', color='blue')
plt.plot(df['Date'], df['SMA20'], label='Średnia 20-dniowa', color='orange')
plt.plot(df['Date'], df['UpperBand'], label='Górna banda Bollingera', color='pink')
plt.plot(df['Date'], df['LowerBand'], label='Dolna banda Bollingera', color='gray')

plt.title('Cena zamknięcia z wskaźnikami Bollingera')
plt.xlabel('Data')
plt.ylabel('Cena')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.xticks(rotation=45)
plt.show()


