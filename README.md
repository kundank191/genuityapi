# GenuityApi
Machine learning model which detects fraud Banknote. link to dataset : https://www.kaggle.com/ritesaluja/bank-note-authentication-uci-data.

I created a machine learning model in jupyter notebook. Which was pickled and stored.
* The pickled model is being used by my app to predict model.
* flask is used to create the backend.
* flasgeer  is used to create the UI.
* Heroku is used to deploy the model.
## This model will be deployed on the net
link for the model : https://genuityapi.herokuapp.com/apidocs/

## Data on which the model is based on.
Data were extracted from images that were taken from genuine and forged banknote-like specimens. For digitization, an industrial camera usually used for print inspection was used. The final images have 400x 400 pixels. Due to the object lens and distance to the investigated object gray-scale pictures with a resolution of about 660 dpi were gained. Wavelet Transform tool were used to extract features from images.
- variance : variance of Wavelet Transformed image
- skweness : skewness of Wavelet Transformed image 
- curtosis : curtosis of Wavelet Transformed image 
- entropy  : entropy of image
- class    : 0 for a fake note, 1 for a genuine note.
Class is the target variable and the rest four are our parameters.


## Images
I am not a front end developer, I am just a python developer, hence the UI is just a functional API screen. The UI was made using Flasgger.

<img src="https://user-images.githubusercontent.com/26672993/84121724-2650e800-aa55-11ea-9eae-53085e52794a.png" width="750" height="500"/>

### Usage
#### Usage for a single case
Click on the Get button. Then click on Test it out, then fill the parameters and then press execute.

<img src="https://user-images.githubusercontent.com/26672993/84121963-6617cf80-aa55-11ea-92d0-51349bcf80e1.png" width="750" height="500"/>

This is the result page, you can see the result in the response body.

<img src="https://user-images.githubusercontent.com/26672993/84122160-a24b3000-aa55-11ea-8aec-66630331cfdb.png" width="750" height="500"/>

#### Usage for a file with multiple cases
Click on the Post button, and select a file.

<img src="https://user-images.githubusercontent.com/26672993/84122274-d161a180-aa55-11ea-8a6f-d7a03d79b466.png" width="750" height="500"/>

- The File should have this format.

<img src="https://user-images.githubusercontent.com/26672993/84122459-1554a680-aa56-11ea-97a1-cec8a2addec5.png" width="300" height="300"/>

This is the result page, you cans see the result in the response body.

<img src="https://user-images.githubusercontent.com/26672993/84122327-e76f6200-aa55-11ea-83a2-125cbcb67a04.png" width="750" height="500"/>


## Heroku limits
Since heroku doesnt allow deployment of more than one project for free, this link might not work in the future. But this repository can be cloned and run in local server.
