import pandas as pd

file = '../data/tweetsAvengersEndgame.csv'

df = pd.read_csv(file, sep=";",encoding = "ISO-8859-1")


print(df)
print(df.head())
#5 rows und 25 columns

print(df.info())
#viel unbenannte
#hashtags, text,created, truncated, screenName, retweetCount, isRetweet, unnamed....

