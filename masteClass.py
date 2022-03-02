from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd


def printTF_IDF(texts):
    records_count = 10
    tfIdfTransformer = TfidfVectorizer(ngram_range=(1, 4), use_idf=True, max_features=records_count)
    countVectorizer = CountVectorizer(ngram_range=(1, 4), max_features=records_count)
    wordCount = countVectorizer.fit_transform([texts])
    TfIdf = tfIdfTransformer.fit_transform([texts])
    names = countVectorizer.get_feature_names()
    df = []
    df = pd.DataFrame(list(names), columns=['names'])
    df = df.assign(Word_Count=wordCount.T.todense())
    df = df.assign(TF_IDF=TfIdf.T.todense())
    # df.insert(1, 'Word_Count', wordCount.T.todense())
    # df.insert(1, 'TF_IDF', TfIdf.T.todense())
    df = df.sort_values('TF_IDF', ascending=False)
    print(df)



if __name__ == "__main__":
    texts = "То есть для каждого слова считается отношение общего количества документов к количеству документов, содержащих данное слово (для частых слов оно будет ближе к 1, для редких слов оно будет стремиться к числу, равному количеству документов), и на логарифм от этого числа умножается исходное значение bag-of-words (к числителю и знаменателю прибавляется единичка, чтобы не делить на 0, и к логарифму тоже прибавляется единичка, но это уже технические детали). После этого в sklearn ещё проводится L2-нормализация каждой строки."
    stexts = texts
    print(texts)
    printTF_IDF(texts)