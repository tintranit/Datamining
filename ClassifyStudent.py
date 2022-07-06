import pandas as pd
df = pd.read_csv('data03.csv')
#KHXH
ells = df.loc[(df['mean'] >= 8 )  & (df['Diali'] > 7) & (df['GDCD'] > 7) & (df['LichSu'] > 7) & (df['Ngoaingu'] > 7) & (df['Nguvan'] > 7) ]
#KHTN
#ells = df.loc[(df['mean'] >= 8 )  & (df['Hoahoc'] > 7) & (df['Sinhhoc'] > 7) & (df['Toan'] > 7) & (df['Vatli'] > 7)]
#filter vat li
#ells = df.loc[(df['mean'] >= 8 ) & (df['Hoahoc'] > 7) & (df['Sinhhoc'] > 7) & (df['Toan'] > 7) ]
print(ells)
#ells.to_csv('temp.csv')
ells.to_csv('HSG/HSG_KHXH.csv', mode='a', header=False)