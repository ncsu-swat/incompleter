#Source: https://stackoverflow.com/questions/48600538/attributeerror-nonetype-object-has-no-attribute-dtype
import numpy as np
import csv
import tensorflow as tf

with open('criminal_train.csv') as fp:
    reader = csv.reader(fp, delimiter=',', quotechar='"')
    train_data = np.array([row for row in reader])
    data_X = train_data[1:, 1:-1]
    data_Y = train_data[1:, -1:]

with open('criminal_test.csv') as fp:
    reader = csv.reader(fp, delimiter=',', quotechar='"')
    test_data = np.array([row for row in reader])
    predict_data = test_data[1:, 1:]

#Spltting the training data in 80:20
split = int(data_X.shape[0]*0.8)
X_train = data_X[:split, :]
X_test = data_X[split:, :]
Y_train_labels = data_Y[:split, :]
Y_test_labels = data_Y[split:, :]

#convert labels to one_hot matrices (classes=2)
Y_train = np.zeros((Y_train_labels.shape[0], 2))
Y_train[np.arange(Y_train_labels.shape[0]), Y_train_labels.astype(int)] = 1
Y_test = np.zeros((Y_test_labels.shape[0], 2))
Y_test[np.arange(Y_test_labels.shape[0]), Y_test_labels.astype(int)] = 1


def random_mini_batches(X, Y, mini_batch_size):
    m = X.shape[0]
    perm = np.random.permutation(X)
    X = X[perm, :]
    Y = Y[perm, :]
    num_batches = int(m / mini_batch_size) + 1
    bathces = []
    for k in range(num_batches):
        X_batch = X[k*mini_batch_size:(k+1)*mini_batch_size, :]
        Y_batch = Y[k*mini_batch_size:(k+1)*mini_batch_size, :]
        batches.append((X_batch, Y_batch))
    return batches

def create_placeholders():
    X = tf.placeholder(tf.float32, shape=[None,70], name='X')
    Y = tf.placeholder(tf.float32, shape=[None,2], name='Y')
    return X, Y

def forward_propagation(X):
    A1 = tf.contrib.layers.fully_connected(X, 100)
    A2 = tf.contrib.layers.fully_connected(A1, 150)
    A3 = tf.contrib.layers.fully_connected(A2, 100)
    Z5 = tf.contrib.layers.fully_connected(A3, 2, activation_fn=None)
    return Z5

def compute_cost(Z5, Y):
    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=Z5, labels=Y))

def model(X_train, X_test, Y_train, Y_test, learning_rate=0.3, beta1=0.9, beta2=0.999, mini_batch_size=32, epochs=1500):
    X, Y = create_placeholders()
    Z5 = forward_propagation(X)
    cost = compute_cost(Z5, Y)
    optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate, beta1=beta1, beta2=beta2).minimize(cost)
    init = tf.global_variables_initializer()

    with tf.Session() as sess:
        sess.run(init)
        for epoch in range(1,epochs+1):
            batches = random_mini_batches(X_train, Y_train, mini_batch_size)
            epoch_cost = 0
            for (X_batch, Y_batch) in batches:
                _, cost = sess.run([optimizer,cost], feed_dict={X:X_batch, Y:Y_batch})
                epoch_cost += cost
            if epoch%100 == 0:
                print('Cost in epoch '+str(epoch)+' is '+str(epoch_cost))
        correct_prediction = tf.equal(tf.argmax(Z5), tf.argmax(Y))
        accuracy = tf.reducce_mean(correct_prediction, 'float')

        print('Train Accuray '+str(accuracy.eval(feed_dict={X:X_train, Y:Y_train})))
        print('Test Accuray '+str(accuracy.eval(feed_dict={X:X_test, Y:Y_test})))

model(X_train, X_test, Y_train, Y_test)