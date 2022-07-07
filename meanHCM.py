import pandas as pd
df = pd.read_csv('HCM/TSHCM.csv')
df['mean'] = df.iloc[: , [2,3,4,7,8,9,10]].mean(axis=1)
print(df)
df.to_csv('HCM/meanHCM.csv')
