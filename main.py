#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Front end for my app

Created on Sun Jun  7 11:09:33 2020

@author: k
"""
from flask import Flask, request
import pandas as pd
import pickle
from flasgger import Swagger

# From here the app will start
app = Flask(__name__)
Swagger(app)

# Load the pickle file, get the classifier
pickle_in = open('classifier.pkl','rb')
classifier = pickle.load(pickle_in)

@app.route('/')
def welcome():
    return 'Find out if a note is fake or not.'

@app.route('/predict')
def predict_note_genuity():
    """Check genuity of a single Bank note
    Ui made using DocString
    ---
    parameters:
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values   
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
    """Check genuity of a file containing list of notes
    Just using DocStrings
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
    responses:
        200:
            description : The output values
        
    """
    df_test = pd.read_csv(request.files.get('file'))
    predictions = classifier.predict(df_test)
    return "Predicted Values for the file " + str(list(predictions))
    
if __name__ == '__main__':
    app.run()





