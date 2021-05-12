import numpy as np
from flask import  Flask, request,render_template,jsonify,url_for
from flask_cors import CORS 
import os
import pickle
import flask
from newspaper import Article
import urllib
import nltk
app= Flask(__name__)
CORS(app)
app= flask.Flask(__name__,template_folder='templates')


path="D:\Codes\Python_Codes\env\model_modified.pkl"
with open(path,'rb') as handle:
    model=pickle.load(handle)

@app.route('/')
def main():
    return render_template('index.html')

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



if __name__=="__main__":
    port =int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0',port=port,debug=True)