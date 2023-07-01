#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    app.py
# @Author:      Kuro
# @Time:        12/09/2022 3:24 PM

import base64
import io

import dash
import dash_bootstrap_components as dbc
import numpy as np
from dash import dcc, html, Output, Input, State
from keras.models import load_model

from utils import preprocess_image

app = dash.Dash(__name__,
                assets_folder="assets",
                assets_url_path="assets",
                external_stylesheets=[
                    dbc.themes.BOOTSTRAP,
                    "https://cdn.jsdelivr.net/gh/lipis/flag-icons@6.6.6/css/flag-icons.min.css"
                ])

app.config['suppress_callback_exceptions'] = True

app.layout = html.Div([
    dbc.Row(
        html.H1('Alopecia Classification', style={'textAlign': 'center', 'font-weight': 'bold', 'margin': 'auto'}),
        style={'background-color': 'rgb(143,188,143)', 'height': '10vh'}
    ),
    html.Div(id='dummy'),
    dbc.Row([
        dbc.Col(html.Label('Select Model: ', style={'font-weight': 'bold', 'float': 'right'})),
        dbc.Col(dcc.Dropdown(
            id='model_dropdown',
            options=['Inception', 'VGG', 'ResNet', 'MobileNet'],
            value='Inception',
            style={'width': '10em'}
        ))
    ], style={'align-items': 'center'}),
    dcc.Upload(
        id='upload-image',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=False
    ),
    html.Hr(),
    html.Div(id='output-image-upload'),
    html.Hr(),
    dcc.Loading(
        id="loading",
        children=html.H5(id='output-prediction', style={'textAlign': 'center', 'font-weight': 'bold'}),
        type="circle",
    )
])


@app.callback(
    Output('dummy', 'children'),
    Input('model_dropdown', 'value'),
)
def update_output(model_name):
    global model
    if model_name == 'Inception':
        model = load_model('models/InceptionV3.h5')
    elif model_name == 'VGG':
        model = load_model('models/VGG16.h5')
    elif model_name == 'ResNet':
        model = load_model('models/ResNet50.h5')
    elif model_name == 'MobileNet':
        model = load_model('models/MobileNet.h5')
    return None


@app.callback(
    Output('output-image-upload', 'children'),
    Input('upload-image', 'contents'),
    State('upload-image', 'filename'),
)
def update_output(data, filename):
    if data is not None:
        return html.Div([html.H5(filename), html.Img(src=data, style={'height': '150px', 'width': '150px'})], style={'textAlign': 'center'})


@app.callback(Output('output-prediction', 'children'),
              Input('upload-image', 'contents'))
def prediction(content):
    if content is None:
        raise dash.exceptions.PreventUpdate
    content_type, content_string = content.split(',')
    content_string = base64.b64decode(content_string)
    buf = io.BytesIO(content_string)
    final_img = preprocess_image(buf)

    result = model.predict(final_img)
    predicted_class_indices = np.argmax(result, axis=1)

    labels = {'Alopecia': 0,
              'Not Alopecia': 1,
              }

    labels = dict((v, k) for k, v in labels.items())
    predictions = [labels[k] for k in predicted_class_indices][0]
    parent_class = predictions.split('___')[0]
    sub_class = predictions.split('___')[-1].replace('_', ' ')

    result_return = 'Prediction: ' + parent_class + " - " + "Prediction class: " + sub_class + " - " + " Accuracy: " + str(round(max(result[0]) * 100, 2)) + "%"
    return result_return


if __name__ == "__main__":
    app.run_server(debug=True)
