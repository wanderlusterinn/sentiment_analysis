import pandas as pd

file = '../data/Me_too.csv'

df = pd.read_csv(file, sep=";",encoding = "ISO-8859-1")


print(df)
print(df.head())
print(df.info())
#8 columns, 41650 Einträge
#TweetID, Conversation ID, Author Id, Author Name, DAteTime, Language, Tweet Text, Hashtags
#int und objects
print(df.describe())