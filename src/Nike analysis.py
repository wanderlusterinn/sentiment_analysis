import pandas as pd
import re
import csv
import preprocessor as p

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

new = new_df["tweet"].str.split("b\'|b\"", n=1, expand=True)
new_df["tweet"] = new[1]

# JULIAN: The problem is, you're doing the operation on all rows, but some
# of your rows do not begin with RT and the stuff behind that. A second problem
# is, that some of your rows also have an underscore in there (example: 2nd row),
# so [a-zA-z] will not work. .* can be used for "everything".
new = new_df["tweet"].str.split("RT\s@+[a-zA-z]+:", n=1, expand=True)

# JULIAN: this does the split better. However, this is going to always give you
# 2 columns (since you specified that), one for the content before and one for
# the content behind the splitting pattern.
# So whenever the pattern exists you're gonna get an empty first column
# and the second column without that pattern, whenever it does not exist, you're
# gonna get everything unchanged in the first column, and "None" in the second:
# there was no split to be made.
new = new_df["tweet"].str.split("RT\s@.*:", n=1, expand=True)

# JULIAN: but I guess you rather want to simply delete the part with "RT...", if
# it exists? Then you could got for str.replace and simply replace the pattern by
# nothing: ""
new = new_df["tweet"].str.replace("RT\s@.*:", "")

# JULIAN: now maybe continue here on your own! :)
new_df["tweet"] = new[1]
new_df["rest"] = new[0]
print(new_df)


tweet_col = new_df["rest"] + new_df["tweet"]
print(tweet_col)


