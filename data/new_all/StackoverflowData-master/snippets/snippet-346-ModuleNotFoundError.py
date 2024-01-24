#Source: https://stackoverflow.com/questions/44309892/typeerror-function-object-is-not-subscriptable-in-tensorflow
import tensorflow as tf
sess = tf.InteractiveSession()
x = tf.placeholder(tf.float32,[None, 784])
W = tf.Variable(tf.zeros[784,10])
b = tf.Variable(tf.zeros[10])