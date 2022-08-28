from crypt import methods
from operator import methodcaller
from flask import Flask, request, render_template
import joblib
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# Create an app object using Flask
app = Flask(__name__)

# Load the model
model = joblib.load('models/model.joblib')

# Use route() to define URL

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    int_features = [float(x) for x in request.form.values()] # convert string to float
    features = np.array(int_features) # convert input to numpy array
    prediction = model.predict(features.reshape(1, -1)) # predict using the loaded model

    if (prediction[0]==0):
        output = 'Normal'
    elif (prediction[0]==1):
        output = 'Abnormal'

    return render_template('index.html', prediction_text='Column is {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)