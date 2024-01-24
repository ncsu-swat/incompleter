#Source: https://stackoverflow.com/questions/57101765/keras-error-on-conv2d-creation-typeerror-cant-multiply-sequence-by-non-int-of
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
import numpy as np


def model():
    new_model = Sequential()
    for i in range(4):
        new_model.add(Conv2D(
                      filters=(3,3), kernel_size = 1
                      , activation='linear', padding='valid'
                      , input_shape=np.array([9,9,9])))

    return cnn_model

if __name__ == '__main__':
    model()