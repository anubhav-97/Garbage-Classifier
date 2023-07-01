from __future__ import division, print_function
# coding=utf-8
import os
import numpy as np

# Keras
from keras.models import load_model
from keras.preprocessing import image

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename

# Defining a Flask app
app = Flask(__name__)

# Model saved with Keras model.save()
MODEL = 'model_cnn.h5'

# Loading the trained model
model = load_model(MODEL)
model.make_predict_function()

def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224))

    # Preprocessing the image
    x = image.img_to_array(img)
    x = np.true_divide(x, 255)
    x = np.expand_dims(x, axis=0)

    # Predicting the model
    preds = model.predict(x)
    return preds


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = model_predict(file_path, model)

        # Process the result for human
        pred_class = np.argmax(preds, axis=1)
        if(pred_class==0):
            result = "Battery"
        elif(pred_class==1):
            result = "Biological"
        elif(pred_class==2):
            result = "Brown Glass"
        elif(pred_class==3):
            result = "Cardboard"
        elif(pred_class==4):
            result = "Clothes"
        elif(pred_class==5):
            result = "Green Glass"
        elif(pred_class==6):
            result = "Metal"
        elif(pred_class==7):
            result = "Paper"
        elif(pred_class==8):
            result = "Plastic"
        elif(pred_class==9):
            result = "Shoes"
        elif(pred_class==10):
            result = "Trash"
        elif(pred_class==11):
            result = "White Glass"
        return result
    return None


if __name__ == '__main__':
    app.run(debug=True)

