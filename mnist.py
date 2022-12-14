# -*- coding: utf-8 -*-
"""MNIST.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wAsbi-RNhK-L97lUcH1AqifKUSOUFQfk
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import tensorflow
import keras

from tensorflow.keras.models import Sequential
from keras.layers import Dense, Dropout
from keras import regularizers
from keras.utils.vis_utils import plot_model

np.random.seed(7)

import warnings
warnings.filterwarnings('ignore')

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

plt.figure(figsize=[10,10])

plt.subplot(2,2,1)
n = 5
plt.imshow(x_train[n], cmap=plt.cm.binary)

plt.subplot(2,2,2)
n = 2
plt.imshow(x_train[n], cmap=plt.cm.binary)

plt.subplot(2,2,3)
n = 3
plt.imshow(x_train[n], cmap=plt.cm.binary)

plt.subplot(2,2,4)
n = 1
plt.imshow(x_train[n], cmap=plt.cm.binary)

plt.suptitle("Some Hand written Digits", size=20, color="#6166B3")

plt.show()

x_train = x_train.reshape(-1, 28*28)
x_train = x_train.astype('float32') / 255

y_train = tensorflow.keras.utils.to_categorical(y_train , num_classes=10)

x_test = x_test.reshape(-1, 28*28)
x_test = x_test.astype('float32') / 255

y_test = tensorflow.keras.utils.to_categorical(y_test , num_classes=10)

nn_model = Sequential()
nn_model.add(Dense(35, input_dim=784, activation='relu'))
nn_model.add(Dropout(0.3))
nn_model.add(Dense(21, activation='relu'))
nn_model.add(Dense(10, activation='softmax'))

plot_model(nn_model, to_file='model.png', show_shapes=True, show_layer_names=True)

nn_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

nn_model.fit(x_train, y_train, epochs=40, batch_size=10)

scores_train = nn_model.evaluate(x_train, y_train)
print("\n%s: %.2f%%" % (nn_model.metrics_names[1], scores_train[1]*100))

scores_test = nn_model.evaluate(x_test, y_test)
print("\n%s: %.2f%%" % (nn_model.metrics_names[1], scores_test[1]*100))

predictions = nn_model.predict(x_test)

plt.figure(figsize=[10,10])

plt.subplot(2,2,1)
n = 0
plt.imshow(x_test[n].reshape(28, 28), cmap=plt.cm.binary)
plt.title("Predicted value: " + str(np.argmax(predictions[n], axis=0)), size=20)

plt.subplot(2,2,2)
n = 1
plt.imshow(x_test[n].reshape(28, 28), cmap=plt.cm.binary)
plt.title("Predicted value: " + str(np.argmax(predictions[n], axis=0)), size=20)

plt.subplot(2,2,3)
n = 2
plt.imshow(x_test[n].reshape(28, 28), cmap=plt.cm.binary)
plt.title("Predicted value: " + str(np.argmax(predictions[n], axis=0)), size=20)

plt.subplot(2,2,4)
n = 3
plt.imshow(x_test[n].reshape(28, 28), cmap=plt.cm.binary)
plt.title("Predicted value: " + str(np.argmax(predictions[n], axis=0)), size=20)

plt.suptitle("Prediction of some Handwritten digits", size=20, color="#6166B3")

plt.show()