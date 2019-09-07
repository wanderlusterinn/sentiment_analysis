import pandas as pd
import string
import re
import nltk
#nltk.download()
from sklearn.feature_extraction.text import CountVectorizer


# file = '../data/tweetsAvengersEndgame.csv'
file = "../data/result_nike_betsyross.csv"

# read in the data
df = pd.read_csv(file, sep=";",encoding = "ISO-8859-1")

# rename columns
df.columns = ['date','time','tweet']

#Nur Wortinhalte behalten
df["tweet"] = df["tweet"].str.replace("b\'|b\"", "")
df["tweet"] = df["tweet"].str.replace("RT\s@.*:", "")

#eigene Funktion erstellen; Punctuation entfernen
def remove_punct(text):
    text  = "".join([char for char in text if char not in string.punctuation])
    text = re.sub('[0-9]+', '', text)
    return text

df['Tweet_punct'] = df['tweet'].apply(lambda x: remove_punct(x))
df.head(10)

#Tokenization
def tokenization(text):
    text = re.split('\W+', text)
    return text

df['Tweet_tokenized'] = df['Tweet_punct'].apply(lambda x: tokenization(x.lower()))
df.head()

#Remove stopwords
stopword = nltk.corpus.stopwords.words('english')


def remove_stopwords(text):
    text = [word for word in text if word not in stopword]
    return text


df['Tweet_nonstop'] = df['Tweet_tokenized'].apply(lambda x: remove_stopwords(x))
df.head(10)

#Stammwörter bilden
ps = nltk.PorterStemmer()

def stemming(text):
    text = [ps.stem(word) for word in text]
    return text

df['Tweet_stemmed'] = df['Tweet_nonstop'].apply(lambda x: stemming(x))
df.head()

#Frage: wie gehen wir mit Nichtwörtern um? Was machen wir damit?

wn = nltk.WordNetLemmatizer()

def lemmatizer(text):
    text = [wn.lemmatize(word) for word in text]
    return text

df['Tweet_lemmatized'] = df['Tweet_nonstop'].apply(lambda x: lemmatizer(x))
df.head()

def delete_stuff(text):
    text = [word for word in text if word.find("http") == -1 and word.find("xx") == -1]
    return text

df['Tweet_ohne_stuff'] = df['Tweet_lemmatized'].apply(lambda x: delete_stuff(x))
df.head()
#Umgang mit Wörtern - exxa, etc.

#eigene Funktion definieren, die alle Schritte vroehr beinhaltet
def clean_text(text):
    text_lc = "".join([word.lower() for word in text if word not in string.punctuation]) # remove puntuation
    text_rc = re.sub('[0-9]+', '', text_lc)
    tokens = re.split('\W+', text_rc)    # tokenization
    text = [ps.stem(word) for word in tokens if word not in stopword]  # remove stopwords and stemming
    text = [word for word in text if word.find("http") == -1 and word.find("xx") == -1]
    return text

#Vectorization
countVectorizer = CountVectorizer(analyzer=clean_text)
countVector = countVectorizer.fit_transform(df['tweet'])
print('{} Number of tweets has {} words'.format(countVector.shape[0], countVector.shape[1]))
# 11412 Number of tweets has 9248 words

n = countVector.shape[0]
m = countVector.shape[1]
#count_vect_df = pd.DataFrame(countVector.toarray(), columns=countVectorizer.get_feature_names())
count_vect_df = pd.DataFrame(countVector[0:n, 0:m].toarray(), columns=countVectorizer.get_feature_names()[0:m])
count_vect_df.head()

# Aussuchen der meistgenannten Wörter - probeweise erstmal die wichtigsten 100 genommen
word_count = count_vect_df.sum(axis=0)
word_count_sorted = word_count.sort_values(ascending=False)
important_words = word_count_sorted[0:100]
important_words.index

# data frame mit den wichtigsten Worten (s.oben)
df_important_words = count_vect_df[important_words.index]

#Wordcloud Visualization
from wordcloud import WordCloud, STOPWORDS , ImageColorGenerator


