import pandas as pd;
from gensim.summarization import summarize, keywords
from summarizer import Summarizer
from rake_nltk import Metric, Rake
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer


def read_dataset(name, num_records):
    dataset = pd.read_csv(name, nrows=num_records);
    return dataset


def BERT_Summarizer(ttext):
    # https: // github.com / dmmiller612 / bert - extractive - summarizer
    # pip install bert-extractive-summarizer
    # pip install ...etc
    model = Summarizer()
    result = model(ttext, min_length=60)
    full = ''.join(result)
    return full


def TextRank_Summarizer(ttext):
    # pip install gensim
    return summarize(str(ttext))


def Rake_Summarizer(ttext):
    r = Rake(language="russian")
    r.extract_keywords_from_text(ttext)
    mas = r.get_ranked_phrases()
    set2 = set()
    for item in mas:
        if not "nan" in str(item).replace(" nan ", " "):
            set2.add(str(item).replace(" nan ", " "))
    mas = list(set2)
    return str(mas)


def TFIDF_Summarizer(ttext):
    records_count = 10
    tfIdfTransformer = TfidfVectorizer(ngram_range=(1, 4), use_idf=True, max_features=records_count)
    countVectorizer = CountVectorizer(ngram_range=(1, 4), max_features=records_count)
    wordCount = countVectorizer.fit_transform([ttext])
    TfIdf = tfIdfTransformer.fit_transform([ttext])
    names = countVectorizer.get_feature_names()
    df = pd.DataFrame(list(names), columns=['names'])
    df = df.assign(Word_Count=wordCount.T.todense())
    df = df.assign(TF_IDF=TfIdf.T.todense())
    df = df.sort_values('TF_IDF', ascending=False)
    return (str(df))


if __name__ == '__main__':
    # dataset = read_dataset('lenta-ru-news.csv', 1000)
    dataset = pd.read_csv("mydataset.csv")
    colums = dataset.columns
    columns = ['title', 'text']
    text = dataset.loc[:, 'text']
    title = dataset.loc[:, 'title']
    mtext = []
    mtitle = []
    mBERT = []
    mTextRank = []
    mRake = []
    mTFIDF = []

    fprint = False     #Печатать в консоль?
    for ind in range(100):
        ttext = text[ind]
        ttitle = title[ind]
        BERT = BERT_Summarizer(ttext)
        TextRank = TextRank_Summarizer(ttext)
        tRake = Rake_Summarizer(ttext)
        TFIDF = TFIDF_Summarizer(ttext)
        if fprint:
            print("\n ---- \n ind = " + str(ind))
            print('\n TEXT: ' + ttext)
            print('\n TITLE: ' + ttitle)
            print('\n BERT: ' + BERT)
            print('\n TextRank: ' + TextRank)
            print('\n Rake: ' + tRake)
            print('\n TFIDF: ' + TFIDF)
        mtext.append(ttext)
        mtitle.append(ttitle)
        mBERT.append(BERT)
        mTextRank.append(TextRank)
        mRake.append(tRake)
        mTFIDF.append(TFIDF)
    df = pd.DataFrame(mtitle, columns=['title'])
    df = df.assign(text=mtext)
    df = df.assign(BERT=mBERT)
    df = df.assign(TextRank=mTextRank)
    df = df.assign(Rake=mRake)
    df = df.assign(TFIDF=mTFIDF)
    df.to_csv("output.csv")
    df.to_excel("output.xls")
