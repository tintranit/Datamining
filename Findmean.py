import csv
import pandas as pd

df = pd.read_csv('datatest.csv')
df.drop(df.columns[[5,6]], axis=1, inplace=True)
df.drop(df.index[0:350000], inplace=True)
df.drop(df.index[350000:701860], inplace=True)
df['mean'] = df.iloc[0:350000, [2,3,4,5,6,7,8,9,10]].mean(axis=1)
print(df)
df.to_csv('data04.csv')

