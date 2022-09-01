import json
from pymystem3 import Mystem

text = "ВАЗЕЛИН - мазеобразная белая жидкость без запаха и вкуса. При неполной очистке цвет меняется от чёрного до жёлтого, при полной - до полупрозрачного. "
ptext = text
m = Mystem()
lemmas = m.lemmatize(text)
mas = m.analyze(text)
outputtext = ""
for item in mas:
    # print(item)
    try:
        analysis = item['analysis']
        text = item['text']
        # print(analysis)
        gr = analysis[0]['gr']
        print(text)
        print(gr)
        print(analysis[0]['lex'])
        outputtext = outputtext + " " + analysis[0]['lex']
        analiz_text = analysis[0]['lex']
        if str.find(analiz_text, "твор"):
            print("+++")
            # print("+++")
        print("_____________")
        WordPart = analysis[0]['gr'][0]
        # print(WordPart)
    except:
        str1 = ""

print(ptext)
print(outputtext)
# print("lemmas:", ''.join(lemmas))
# print("full info:", json.dumps(m.analyze(text), ensure_ascii=False))
#


# lemmas: красивый мама красиво мыть рама

# full info: [{"text": "Красивая", "analysis": [{"lex": "красивый", "gr": "A=им,ед,полн,жен"}]}, {"text": " "}, {"text": "мама", "analysis": [{"lex": "мама", "gr": "S,жен,од=им,ед"}]}, {"text": " "}, {"text": "красиво", "analysis": [{"lex": "красиво", "gr": "ADV="}]}, {"text": " "}, {"text": "мыла", "analysis": [{"lex": "мыть", "gr": "V,несов,пе=прош,ед,изъяв,жен"}]}, {"text": " "}, {"text": "раму", "analysis": [{"lex": "рама", "gr": "S,жен,неод=вин,ед"}]}, {"text": "\n"}]
