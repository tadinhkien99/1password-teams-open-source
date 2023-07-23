#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    api.py
# @Author:      kien.tadinh
# @Time:        6/20/2023 11:46 PM

from flask import Flask, request, jsonify
import numpy as np
from PIL import Image
from tensorflow import keras

app = Flask(__name__)
model = keras.models.load_model('models/InceptionV3.h5')

def preprocess_image(image):
    # Preprocess the image for model prediction
    img = image.resize((224, 224))  # Resize to the input shape of your model
    img = img.convert('RGB')  # Convert to RGB if necessary
    img = np.array(img)  # Convert PIL Image to NumPy array
    img = img / 255.0  # Normalize pixel values between 0 and 1
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'})

    image = request.files['image']
    img = Image.open(image)
    img = preprocess_image(img)

    # Perform prediction using the loaded model
    prediction = model.predict(img)
    predicted_class = np.argmax(prediction, axis=1)[0]
    labels = {'Alopecia': 0,
              'Not Alopecia': 1,
              }

    labels = dict((v, k) for k, v in labels.items())
    predictions = labels[int(predicted_class)]

    return jsonify({'predicted_class': predictions})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8100)



