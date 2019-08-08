import pandas as pd

file = "../_data/result_nike_betsyross.csv"

df = pd.read_csv(file, sep=';', header = None)
df.columns = ['date','time','tweet']

print(df)
