from __future__ import absolute_import, division, print_function

import os
import tensorflow as tf
from tensorflow import keras

class SongNN:
    class_names = ['Joy', 'Sadness', 'Anger', 'Disgust', 
                   'Trust', 'Fear', 'Suprise', 'Anticipation']
    def __init__(self):
        self.model = self.makeModel

    def makeModel(self):
        model = keras.Sequential([
            keras.layers.Dense(13),
            keras.layers.Dense(128, activation=tf.nn.relu),
            keras.layers.Dense(64, activation=tf.nn.relu),
            keras.layers.Dense(8, activation=tf.nn.softmax)
        ])
        model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])
        return model

sNN = SongNN()
sNN.    
