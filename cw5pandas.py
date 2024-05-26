import pandas as pd
import numpy as np

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
s = pd.Series([10, 12 , 8, 14], index=['a','b','c','d'])
print(s)
data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
        'Stolica': ['Bruksela', 'New Delhi', 'brasilia'],
        'Populacja': [123131, 11251235235, 15235235]}
df = pd.DataFrame(data)
print(df)
print(df.dtypes)
df = pd.read_csv('dane.csv', header=0, sep=";", decimal='.')
print(df)
df.to_csv('plik.csv', index=False)

print(s['c'])
print(s.c)
print(df[0:1])
print("")
print(df['Populacja'])
print(df.ilosc[0, 0])
print(df.loc[0, "Kraj"])
print(df.at[0, "Kraj"])
