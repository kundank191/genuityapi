#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create a Flask app

Created on Sun Jun  7 10:22:53 2020

@author: k

from flask import Flask, request
import pandas as pd
import pickle

# From here the app will start
app = Flask(__name__)

# Load the pickle file, get the classifier
pickle_in = open('classifier.pkl','rb')
classifier = pickle.load(pickle_in)

@app.route('/')
def welcome():
    """
    The slash in the route says that this is the root
    user will see this message first
    
    Returns
    -------
    str
        Just a message.

    """
    return 'Find out if a note is fake or not.'

@app.route('/predict')
def predict_note_genuity():
    """
    By default this function is a get function
    
    
    Returns whether the note is genuine or not based on parameters
    -------
    API will predict, using 4 parameters, because our model was trained on 4 variables

    """
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy  = request.args.get('entropy')
    # using these variables to predict if the note was genuine
    prediction = classifier.predict([[variance,
                                      skewness,
                                      curtosis,
                                      entropy]])
    
    if prediction == 1:
        return "Genuine note"
    else:
        return "Fake note"

@app.route('/predict_file', methods = ['POST'])
def predict_file_genuity():
    """
    Get a file of various values and predict for every row

    Returns
    -------
    Str
        Result of genuity for every row.

    """
    df_test = pd.read_csv(request.files.get('file'))
    predictions = classifier.predict(df_test)
    return "Predicted Values for the file " + str(list(predictions))
    
if __name__ == '__main__':
    app.run()


"""
