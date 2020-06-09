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

<img src="https://user-images.githubusercontent.com/26672993/84121724-2650e800-aa55-11ea-9eae-53085e52794a.png" width="800" height="450"/>

### Usage
#### Usage for a single case
Click on the Get button. Then click on Test it out, then fill the parameters and then press execute.

<img src="https://user-images.githubusercontent.com/26672993/84123980-33bba180-aa58-11ea-8099-2293d35721b9.png" width="800" height="450"/>

This is the result page, you can see the result in the response body.

<img src="https://user-images.githubusercontent.com/26672993/84124068-56e65100-aa58-11ea-8953-3c75015f5b78.png" width="800" height="450"/>

#### Usage for a file with multiple cases
Click on Try it out then, click on the Post button, and select a file.

<img src="https://user-images.githubusercontent.com/26672993/84124235-9319b180-aa58-11ea-9591-0da6bffc77d6.png" width="800" height="450"/>

- The File should have this format.

<img src="https://user-images.githubusercontent.com/26672993/84122459-1554a680-aa56-11ea-97a1-cec8a2addec5.png" width="300" height="300"/>

This is the result page, you cans see the result in the response body.

<img src="https://user-images.githubusercontent.com/26672993/84124320-b04e8000-aa58-11ea-8f97-1546737ab2b2.png" width="800" height="450"/>


## Heroku limits
Since heroku doesnt allow deployment of more than one project for free, this link might not work in the future. But this repository can be cloned and run in local server.
