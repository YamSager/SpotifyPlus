from __future__ import absolute_import, division, print_function

import os
import tensorflow as tf
from tensorflow import keras

import numpy as np

print(tf.__version__)

def process(array, size): 
    arrayOut = []
    dictionary = {}
    newWord = 1
    for i in range(size):
        if i >= len(array):
            arrayOut.append(0)
    if os.path.isfile('dataDic.txt','r'):
        dicFile = open('dataDic.txt', 'rw')
        dictionary = dicFromFile(dicFile)
        newWord = len(dictionary.keys())
    for i in range(size):
        if i >= len(array):
            arrayOut.append(0)
        else:
            if (array[i] not in dictionary.keys()):
                dictionary[array[i]] = newWord
                newWord += 1
            arrayOut.append(dictionary[array[i]])
    return arrayOut

def makeModel():
    model = keras.Sequential()
    model.add(keras.layers.Embedding(10000, 16))
    model.add(keras.layers.GlobalAveragePooling1D())
    model.add(keras.layers.Dense(16, activation=tf.nn.relu)) 
    model.add(keras.layers.Dense(1, activation=tf.nn.sigmoid))
    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['acc'])
    return model

def main():
    train_data = input("Enter Filename: ")
    train_data = open(train_data)
    
