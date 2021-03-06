import numpy as np
from flask import  Flask, request,render_template,jsonify,url_for
from flask_cors import CORS 
import os
import pickle5 as pickle
import flask
from newspaper import Article
import urllib
import nltk
app= Flask(__name__)
CORS(app)
app= flask.Flask(__name__,template_folder='templates')

pickle_in=open('model_modified','rb')
model=pickle.load(pickle_in)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])
def predict():
    url = request.form['url']
    url = urllib.parse.unquote(url)
    article = Article(str(url))
    article.download()
    article.parse()
    article.nlp()
    news = article.summary
    pred = model.predict([news])
    if pred[0] == 1:
        result = "TRUE"
    else:
        result = "FALSE"

    finalResult={
        'url':url,
        'result':result
    }
    return (str(result))

@app.route('/checknews',methods=['POST','GET'])
def checknews():
    url = request.get_data(as_text=True)[5:]
    url = urllib.parse.unquote(url)
    article = Article(str(url))
    article.download()
    article.parse()
    article.nlp()
    news = article.summary
    pred = model.predict([news])
    if pred[0] == 1:
        result = "TRUE"
    else:
        result = "FALSE"
    return render_template('result.html'.format(result))

if __name__=="__main__":
    app.run(debug=True)
