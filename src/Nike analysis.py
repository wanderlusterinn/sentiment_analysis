import pandas as pd

# determine the path for the data
file = "../data/result_nike_betsyross.csv"

# create a dataframe
# seperate the csv in columns after ;
df = pd.read_csv(file, sep=';', header = None)

# creating a header/naming the columns
df.columns = ['date','time','tweet']

# deleting all columns besides 'tweet'
# create a new csv file
keep_col = ['tweet']
new_df = df[keep_col]
new_df.to_csv("tweetsnike.csv", index=False)

print(new_df)

# dropping null value columns to avoid errors
new_df.dropna(inplace = True)

# new data frame with split value columns
new = new_df["tweet"].str.split("b'", n = 1, expand = True)
# making separate b' columns
new_df["b'"] = new[0]
# making separate tweet column
new_df["tweet"] = new[1]

print(new_df)