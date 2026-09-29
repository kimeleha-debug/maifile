import pandas as pd

data = ("C:\\Users\\user\\OneDrive\\Desktop\\ДЗ\\dz (1).csv")
 
df = pd.read_csv(data, sep = ";")

#pd.set_option("display.max.columns",None)

print(df.head())

print("Таблица данных:")

print(data)

print("\nЗначения CTR:")

print(df['CTR, %'])
