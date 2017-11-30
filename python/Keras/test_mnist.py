
import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.layers import Conv2D, MaxPooling2D, Flatten
from keras.optimizers import SGD, Adam
from keras.utils import np_utils
from keras.datasets import mnist

def load_data():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    number = 5
    x_train = x_train[0:number]
    print "x_train: "
    print x_train
    print "x_train dim: ", x_train.ndim
    print x_train.shape

if __name__ == '__main__':
    load_data()
