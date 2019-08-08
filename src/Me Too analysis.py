import pandas as pd

file = r'C:\Users\Natalja\PycharmProjects\TwitterSquad\venv\Me too camapaign.csv'

df = pd.read_csv(file, sep=";",encoding = "ISO-8859-1")


print(df)
print(df.head())
print(df.info())
print(df.describe())