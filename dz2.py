import string
from nltk.corpus import stopwords
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer

with open('dz_ex.txt', "r", encoding='utf-8') as file:
    texts = file.read()
print(texts)

str2 = ''
for item in texts.split():
    str2 = str2 + ' ' + item
texts = str(texts)
texts = texts.lower()
# print(texts)
texts = texts.replace('\n', ' ')

str2 = ''
for c in texts:
    if c not in ('0', "1", '2', '3', '4', '5', '6', '7', '8', '9', '«', '»', '–', "\""):
        str2 = str2 + c
texts = str2

str2 = ''
pattern = string.punctuation
for c in texts:
    if c not in pattern:
        str2 = str2 + c
    else:
        str2 = str2 + " "
texts = str2
str2 = ''

russian_stopwords = stopwords.words("russian")
for word in texts.split():
    if word not in (russian_stopwords):
        str2 = str2 + " " + word
texts = str2

str2 = ''
for word in texts.split():
    if len(word) > 1:
        str2 = str2 + " " + word
texts = str2
print(texts)

records_count = 30
tfIdfTransformer = TfidfVectorizer(ngram_range=(1, 4), use_idf=True, max_features=records_count)
countVectorizer = CountVectorizer(ngram_range=(1, 4), max_features=records_count)
wordCount = countVectorizer.fit_transform([texts])
TfIdf = tfIdfTransformer.fit_transform([texts])
names = countVectorizer.get_feature_names()

df = pd.DataFrame(list(names), columns=['names'])
df = df.assign(Word_Count=wordCount.T.todense())
df = df.assign(TF_IDF=TfIdf.T.todense())
df = df.sort_values('TF_IDF', ascending=False)
print(df)