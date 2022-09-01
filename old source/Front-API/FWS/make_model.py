import re
from pymorphy2 import MorphAnalyzer
from nltk.corpus import stopwords
import os
from gensim.models import FastText

def lemmatize(doc):
    # doc = re.sub(patterns, ' ', doc)
    patterns = "[A-Za-z0-9!#$%&'()*+,./:;<=>?@[\]^_`{|}~—\"\-«»]+"
    stopwords_ru = stopwords.words("russian")
    morph = MorphAnalyzer()
    doc = re.sub(patterns, ' ', doc)
    tokens = []
    for token in doc.split():
        if token and token not in stopwords_ru:
            token = token.strip()
            token = morph.normal_forms(token)[0]
            if len(token)>2:
                tokens.append(token)
    if len(tokens) > 2:
        text=""
        for item in tokens:
            text=text + " " + item
        return text
    return ""

def get_text():
    #Подготовка файла и обучение модели
    texts=""
    for i in range(1,2):
        with open('static/data/'+str(i)+'.txt', "r", encoding='cp1251') as file_object:
            text = file_object.read()
            texts+=text

    # убрать пустые строки
    import nltk
    nltk.download('stopwords')
    new_texts=""
    row=0
    print(len(texts.split('\n')))
    for item in texts.split('\n'):
        item = lemmatize(item)
        row+=1
        print(row)
        if len(item)>2:
            new_texts = new_texts + '\n' + str(item)
    texts=new_texts
    with open('static/alltexts.txt', 'w') as the_file:
        the_file.write(texts)

def print_text():
    texts=""
    for i in range(1,2):
        with open('static/data/'+str(i)+'.txt', "r", encoding='cp1251') as file_object:
            text = file_object.read()
            texts+=text
    print(texts)


def make_model():
    flat_list = []
    with open('static/alltexts.txt') as f:
        flat_list = [line.split() for line in f]
    ft_mod = FastText(workers=8)
    ft_mod.build_vocab(flat_list)
    ft_mod.train(flat_list, total_examples=ft_mod.corpus_count, epochs=30)
    ft_mod.save('static/model.model')

def sim():
    ft_mod = FastText.load('static/model.model')
    text=""
    # with open('static/alltexts.txt', 'r') as file_object:
    #     text = file_object.read()

    # wordMas = data['words'].split(" ")
    wordMas=[]
    # wordMas.append("тыл")
    # wordMas.append("мальчик")
    # wordMas.append("девочка")
    # wordMas.append("пулемет")
    # wordMas.append("винтовка")
    # wordMas.append("бомба")
    # wordMas.append("боря")
    wordMas.append("сириец")


    # for word in wordMas:
    #     compare = ft_mod.wv.similarity(text, word)
    #     print(compare)
    for word in wordMas:
        similarities = ft_mod.wv.most_similar(positive=[word])
        print(similarities)


if __name__ == '__main__':
    # print_text()
    # get_text()
    make_model()
    # sim()