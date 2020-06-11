# GenuityApi
Machine learning model which detects fraud Banknote. link to dataset : https://www.kaggle.com/ritesaluja/bank-note-authentication-uci-data.

I created a machine learning model in jupyter notebook. Which was pickled and stored.
* The pickled model is being used by my app to predict model.
* flask is used to create the backend.
* flasgeer  is used to create the UI.
* Heroku is used to deploy the model.
## This model will be deployed on the net
link for the model : https://genuityapi.herokuapp.com/

## Data on which the model is based on.
Data were extracted from images that were taken from genuine and forged banknote-like specimens. For digitization, an industrial camera usually used for print inspection was used. The final images have 400x 400 pixels. Due to the object lens and distance to the investigated object gray-scale pictures with a resolution of about 660 dpi were gained. Wavelet Transform tool were used to extract features from images.
- variance : variance of Wavelet Transformed image
- skweness : skewness of Wavelet Transformed image 
- curtosis : curtosis of Wavelet Transformed image 
- entropy  : entropy of image
- class    : 0 for a fake note, 1 for a genuine note.
Class is the target variable and the rest four are our parameters.


## Usage

<img src="https://user-images.githubusercontent.com/26672993/84376831-4f14e100-abff-11ea-9b50-e3f5c90a71ee.gif" width="820" height="400" />

