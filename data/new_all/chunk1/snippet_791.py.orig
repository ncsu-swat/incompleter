#Source: https://stackoverflow.com/questions/51870801/typeerror-fetch-argument-none-has-invalid-type-class-nonetype-in-tensorflow
import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.datasets import load_boston
import matplotlib.pyplot as plt

boston=load_boston()
type(boston)
boston.feature_names

bd=pd.DataFrame(data=boston.data,columns=boston.feature_names)

bd['Price']=pd.DataFrame(data=boston.target)
np.random.shuffle(bd.values)


W0=tf.Variable(0.0000000003)
W1=tf.Variable(0.000000000002)
b=tf.Variable(0.0000000000001)
    #print(bd.shape[1])

    #tf.summary.histogram('Weights', W0)
    #tf.summary.histogram('Weights', W1)
    #tf.summary.histogram('Biases', b)



dataset_input=bd.iloc[:, 0 : bd.shape[1]-1];
    #dataset_input.head(2)

dataset_output=bd.iloc[:, bd.shape[1]-1]
dataset_output=dataset_output.values
dataset_output=dataset_output.reshape((bd.shape[0],1)) #converted (506,) to (506,1) because in pandas
    #the shape was not changing and it was needed later in feed_dict


dataset_input=dataset_input.values  #only dataset_input is in DataFrame form and converting it into np.ndarray

    # ADDED
dataset_input = np.array(dataset_input, dtype=np.float32)
    # ADDED
dataset_output = np.array(dataset_output, dtype=np.float32)

X=tf.placeholder(tf.float32, shape=(None,bd.shape[1]-1))
Y=tf.placeholder(tf.float32, shape=(None,1))

Y_=W0*X*X + W1*X + b
    #Y_pred = tf.add(tf.multiply(tf.pow(X, pow_i), W), Y_pred)
print(X.shape)
print(Y.shape)


loss=tf.reduce_mean(tf.square(Y_-Y))
    #tf.summary.scalar('loss',loss)

optimizer=tf.train.GradientDescentOptimizer(0.0000000000001)
train=optimizer.minimize(loss)

init=tf.global_variables_initializer()#tf.global_variables_initializer()#tf.initialize_all_variables()
sess=tf.Session()
sess.run(init)



wb_=[]
with tf.Session() as sess:
    summary_merge = tf.summary.merge_all()

    writer=tf.summary.FileWriter("Users/ajay/Documents",sess.graph)

    epochs=10
    sess.run(init)

    for i in range(epochs):
        s_mer=sess.run(summary_merge,feed_dict={X: dataset_input, Y: dataset_output})  #ERROR________ERROR
        sess.run(train,feed_dict={X:dataset_input,Y:dataset_output})

            #CHANGED
        print("loss",sess.run(loss, feed_dict={X:dataset_input,Y:dataset_output}))
        #sess.run(loss, feed_dict={X:dataset_input,Y:dataset_output})
        writer.add_summary(s_mer,i)

            #tf.summary.histogram(name="loss",values=loss)
        if(i%5==0):
            print(i, sess.run([W0,W1,b]))
            wb__.append(sess.run([W0,W1,b]))

        print(writer.get_logdir())
        print(writer.close())