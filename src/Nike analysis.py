import pandas as pd

file = "../data/result_nike_betsyross.csv"

df = pd.read_csv(file, sep=';', header = None)
df.columns = ['date','time','tweet']

print(df)
df.head()
#Columns date, time, tweet

df.describe()
#11413 Einträge
df.info()