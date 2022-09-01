import string
from nltk.corpus import stopwords
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer


class TextAnalyseTFIDF:
    data = ""

    def __init__(self):
        self.data = ""

    def load_data(self, filename='data.txt'):
        with open(filename, "r", encoding='utf-8') as file:
            self.data = file.read()

    def remove_digit(self):
        str2 = ''
        for c in self.data:
            if c not in ('0', "1", '2', '3', '4', '5', '6', '7', '8', '9', '«', '»', '–', "\""):
                str2 = str2 + c
        self.data = str2

    def remove_punctuation(self):
        str2 = ''
        pattern = string.punctuation
        for c in self.data:
            if c not in pattern:
                str2 = str2 + c
            else:
                str2 = str2 + ""
        self.data = str2

    def remove_stopwords(self):
        str2 = ''
        russian_stopwords = stopwords.words("russian")
        for word in self.data.split():
            if word not in (russian_stopwords):
                str2 = str2 + " " + word
        self.data = str2

    def remove_short_words(self, length=1):
        str2 = ''
        for line in self.data.split("\n"):
            str3 = ""
            for word in line.split():
                if len(word) > length:
                    str3 += " " + word
            str2 = str2 + "\n" + str3
        self.data = str2

    def remove_paragraf_to_lower(self):
        self.data = self.data.lower()
        self.data = self.data.replace('\n', ' ')

    def print_TFIDF(self,records_count = 10):
        tfIdfTransformer = TfidfVectorizer(ngram_range=(1, 4), use_idf=True, max_features=records_count)
        countVectorizer = CountVectorizer(ngram_range=(1, 4), max_features=records_count)
        wordCount = countVectorizer.fit_transform([self.data])
        TfIdf = tfIdfTransformer.fit_transform([self.data])
        names = countVectorizer.get_feature_names()

        df = pd.DataFrame(list(names), columns=['names'])
        df = df.assign(Word_Count=wordCount.T.todense())
        df = df.assign(TF_IDF=TfIdf.T.todense())
        df = df.sort_values('TF_IDF', ascending=False)
        print(df)

if __name__ == '__main__':
    TF = TextAnalyseTFIDF()

    TF.load_data()
    print("Исходный текст:")
    print(TF.data)
    print("")

    TF.remove_digit()
    print("Убрали все цифры:")
    print(TF.data)
    print("")

    TF.remove_punctuation()
    print("Убрали все знаки припинания:")
    print(TF.data)
    print("")

    TF.remove_punctuation()
    print("Убрали все стоп слова:")
    print(TF.data)
    print("")

    TF.remove_short_words(3)
    print("Убрали все слова из 1й буквы:")
    print(TF.data)
    print("")

    TF.remove_paragraf_to_lower()
    print("Убрали все переносы строк и привести в нижний регистр:")
    print(TF.data)
    print("")

    TF.print_TFIDF()
    print("")


