#Source: https://stackoverflow.com/questions/59585574/autograph-in-tensorflow-1-15-gives-typeerror-in-conditional-statement-with-value
import tensorflow as tf
from tensorflow import autograph as ag

#minimal code for method to demonstrate issue
def foo(x):
    if x > 0:
        y = x * x
    else:
        y = 0.0
    return y

#graph construction
mdl = tf.Graph()
with mdl.as_default():
    converted_foo = ag.to_graph(foo)
    print(ag.to_code(foo))
    x = tf.placeholder(tf.double, name='x')
    y = converted_foo(x)