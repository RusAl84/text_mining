import pymorphy2

text_ru = u'Где твоя ложка, папа?'
pymorph = pymorphy2.MorphAnalyzer()

for word in text_ru.split(u’ ’):
    if re.match(u'([^ a-zа-яe¨]+)', word):
        word = pymorph.parse(word)[0].normal_form
    print(word)
