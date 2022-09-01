from flask import Flask, request, jsonify
from gensim.models import FastText
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/api/most_similar', methods=["POST", "GET"])
def get_most_similar():
    if request.method == "POST":
        data = request.json
        word = data['word']
        print(word)
        ft_mod = FastText.load('static/model.model')
        similarities = ft_mod.wv.most_similar(positive=[word])
        print(similarities)
        return jsonify(similarities)


if __name__ == '__main__':
    app.run()
