import pandas as pd
df = pd.read_csv('HCM/meanHCM.csv')
KHTN = df.loc[(df['mean'] >= 8 )    & (df['Diali'] >= 7) & (df['GDCD'] >=7 ) 
& (df['LichSu'] >= 7) & (df['Ngoaingu'] >= 7) & (df['Nguvan'] >= 7) ]
#KHTN
KHXH = df.loc[(df['mean'] >= 8 ) & (df['Hoahoc'] >=7) & (df['Sinhhoc'] >=7) 
& (df['Toan'] >=7) & (df['Vatli'] >=7)]
print(KHXH)
print(KHTN)
KHTN.to_csv('HCM/HSG_HCM.csv')
KHXH.to_csv('HCM/HSG_HCM.csv', mode='a', header=False)