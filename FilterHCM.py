import pandas as pd
df = pd.read_csv('Full_Mark_2020.csv')
#HCM = df.loc[(df['Toan'] )  ]
print(df['Toan'])
#HCM.to_csv('HCM/TSHCM.csv')
#ells.to_csv('HSG/HSG_KHXH.csv', mode='a', header=False)