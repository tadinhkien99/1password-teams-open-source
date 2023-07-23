#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    utils.py
# @Author:      Kuro
# @Time:        12/09/2022 3:25 PM

import numpy as np
from PIL import Image
from keras.models import load_model


# def load_trained_model():
#     model = load_model('models/InceptionV3.h5')
#     return model


def preprocess_image(buf):
    image = Image.open(buf).convert('RGB').resize((224, 224))
    image = np.array(image).reshape(1, 224, 224, 3)
    image = image / 255
    return image
