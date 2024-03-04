#Source: https://stackoverflow.com/questions/45583691/typeerror-expected-string-or-bytes-like-object-tensorflow
import tensorflow as tf
with tf.Session() as ses:
    c = tf.add(1, 2)
    d = ses.run(c)
    print(d)