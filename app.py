import numpy as np
from flask import  Flask, request,render_template,jsonify
from flask_cors import CORS 
import os
import json
import pickle
import flask
import newspaper
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
    #url = request.get_json
    return render_template('index.html')

@app.route('/json',methods=['POST','GET'])
def check():
    data = request.get_json
    return jsonify(data)

@app.route('/predict',methods=['POST','GET'])
def predict():
    '''
    data = request.get_json()
    #url = data('url')
    url = request.get_data(as_text=True)[5:]
    url = urllib.parse.unquote(url)
    article = Article(str(url))
    article.download()
    article.parse()
    article.nlp()
    news = article.summary
    pred = model.predict([news])   
    #accuracy = model.score([news])
    if pred[0] == 1:
        result = "TRUE"
    else:
        result = "FALSE"

    finalResult={
        'url':url,
        'result':result
    }
    '''
    return render_template('result.html')

if __name__=="__main__":
    port =int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0',port=port,debug=True)