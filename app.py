# -*- coding: utf-8 -*-

import numpy as np
import pickle
from flask import Flask, request, render_template

# Load ML model
model = pickle.load(open('model.pkl', 'rb')) 

# Create application
app = Flask(__name__)

# Bind home function to URL
@app.route('/')
def home():
    return render_template('index.html')

# Bind predict function to URL
@app.route('/predict', methods =['POST'])
def predict():
    
    # Put all form entries values in a list 


    features = [float(i) for i in request.form.values()]

    array_features = [np.array(features)]

    # data1 = request.form.values['age']
    # data2 = request.form.values['sex']
    # data3 = request.form.values['cp']
    # data4 = request.form.values['trestbps']
    # data5 = request.form.values['chol']
    # data6 = request.form.values['fbs']
    # data7 = request.form.values['restecg']
    # data8 = request.form.values['thalach']
    # data9 = request.form.values['exang']
    # data10 = request.form.values['oldpeak']
    # data11 = request.form.values['slope']
    # data12 = request.form.values['ca']
    # data13 = request.form.values['thal']
    # # # Convert features to array
    # array_features = [np.array([[data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13]])]
    # Predict features
    prediction = model.predict(array_features)
    
    output = prediction
    
    # Check the output values and retrive the result with html tag based on the value
    if output == 1:
        return render_template('index.html', 
                               result = 'The patient is not likely to have heart disease!')
    else:
        return render_template('index.html', 
                               result = 'The patient is likely to have heart disease!')

if __name__ == '__main__':
#Run the application
    app.run()
    