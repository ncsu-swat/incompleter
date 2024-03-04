#Source: https://stackoverflow.com/questions/50678620/typeerror-input-b-of-matmul-op-has-type-float32-that-does-not-match-type-in
import tensorflow as tf
import numpy as np

x = ([[3, 4, 5], [1, 2, 3], [3, 2, 5]])
y = ([[1, 2, 3, 4, 5, 6, 7, 8], [5, 3, 2, 5, 2, 6, 2, 5], [3, 2, 2, 5, 2, 4, 2, 7]])

tf.cast(x, tf.float32)
tf.cast(y, tf.float32)

train_x = np.asarray([3.3, 4.4, 5.5, 6.71, 6.93, 4.168, 9.779, 6.182, 7.59, 2.167,
    7.042, 10.791, 5.313, 7.997, 5.654, 9.27, 3.1], dtype=float)
train_y = np.asarray([1.7, 2.76, 2.09, 3.19, 1.694, 1.573, 3.366, 2.596, 2.53, 1.221,
    2.827, 3.465, 1.65, 2.904, 2.42, 2.94, 1.3], dtype=float)

learning_rate = 0.01
training_epochs = 100
batch_size = 10

n_hidden_1 = 256  # number of neurons in first hidden layer
n_hidden_2 = 256  # ,,      ...      ,,, second hidden layer
n_input = 50  # Dimension of feature used
n_output = 8  # Number of output neurons

weights = {
    'hidden_1': tf.Variable(tf.random_normal([n_input, n_hidden_1])),  # Randomly initialising weights
    'hidden_2': tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2])),  # Randomly initialising weights
    'out': tf.Variable(tf.random_normal([n_hidden_2, n_output]))
}
biases = {
    'b1': tf.Variable(tf.random_normal([n_hidden_1])),
    'b2': tf.Variable(tf.random_normal([n_hidden_2])),
    'out': tf.Variable(tf.random_normal([n_output]))
}


def mlp(_x, _weights, _biases):  # Feed forward net / Multi layer perceptron
    # Defining layers

    layer_1 = tf.nn.relu(tf.add(tf.matmul(_x, _weights['hidden_1']), _biases['b1']))
    # Choose appropriate activation here
    layer_2 = tf.nn.relu(tf.add(tf.matmul(layer_1, _weights['hidden_2']), _biases['b2']))
    # layer_2 = tf.nn.relu()

    # Linear activation for output
    out_layer = tf.add(tf.matmul(layer_2, _weights['out']), _biases['out'])
    return out_layer


prediction = mlp(x, weights, biases)