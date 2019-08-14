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

# JULIAN: You have almost had it there! The problem is, that you need something
# called regular expressions ("regex") to define the split. The symbol you want
# to split on is " or ', which are special symbols in Python (and R), since they
# define the beginning of a string (as in path = "your_file.csv" for example). So
# in order to use them as a character, you need to put an "escape"-character in
# front of them, which is a backslash \. The expression below now works and does
# a second thing: with | you can say "or", so this splits on either
# b' or b".

# new data frame with split value columns
new = new_df["tweet"].str.split("b\'|b\"", n = 1, expand = True)
# making separate tweet column
new_df["tweet"] = new[1]

print(new_df)