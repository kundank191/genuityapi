#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Front end for my app

Created on Sun Jun  7 11:09:33 2020

@author: k
"""
from flask import Flask, request, render_template
import pandas as pd
import pickle

# From here the app will start
app = Flask(__name__, template_folder = 'templates')
# Load the pickle file, get the classifier
pickle_in = open('model/classifier.pkl','rb')
classifier = pickle.load(pickle_in)

@app.route('/')
def welcome():
    return render_template('main.html')

@app.route('/predict', methods = ['POST'])
def predict():
    variance = request.form['variance']
    skewness = request.form['skewness']
    curtosis = request.form['curtosis']
    entropy  = request.form['entropy']
    # using these variables to predict if the note was genuine
    prediction = classifier.predict([[variance,
                                      skewness,
                                      curtosis,
                                      entropy]])
    result = get_formatted_prediction(prediction)
    return render_template('result.html',result = result)

@app.route('/predict_file', methods = ['GET','POST'])
def predict_file():
    # read the file
    df_test = pd.read_csv(request.files['file'])
    # do the prediction
    prediction = classifier.predict(df_test)
    # format the result
    result = get_formatted_prediction(prediction)
    return render_template('result.html', result = result)
    
def get_formatted_prediction(prediction):
    if len(prediction) == 1:
        if prediction[0] == 0:
            return "It is a Fake note"
        else:
            return "It is a Genuine note"
    result = ""
    for i in range(len(prediction)):
        if prediction[i] == 0:
            result += str(i+1) + " is a Fake note" +"\n"
        else:
            result += str(i+1) + " is a Genuine note" +"\n"
    return result
if __name__ == '__main__':
    app.run()





