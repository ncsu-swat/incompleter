#Source: https://stackoverflow.com/questions/65366442/cannot-convert-a-symbolic-keras-input-output-to-a-numpy-array-typeerror-when-usi
import tensorflow as tf
import numpy as np

 
TextVectorization = tf.keras.layers.experimental.preprocessing.TextVectorization

class SampledSoftmaxLoss: #(tf.keras.losses.Loss):

  def __init__(self, model, n_classes):
    self.model = model
    output_layer = model.layers[-1]
    self.input = output_layer.input
    self.weights = output_layer.weights
    self.n_classes = n_classes


  def loss(self, y_true, y_pred, **kwargs):
    labels = tf.argmax(y_true, axis=1)
    labels = tf.expand_dims(labels, -1)
    loss = tf.nn.sampled_softmax_loss(
        weights=self.weights[0],
        biases=self.weights[1],
        labels=labels,
        inputs=self.input,
        num_sampled = 3,
        num_classes = self.n_classes
    )
    return loss


max_features = 50  # Maximum vocab size.
max_len = 10  # Sequence length to pad the outputs to.
embedding_dims = 5

input_data = np.array([ 
    "Python Machine Learning",
    "Data Science from Scratch: First Principles with Python", 
    "Hands-On Machine Learning with Scikit-Learn and TensorFlow: Concepts, Tools, and Techniques for Building Intelligent Systems",
    "Introduction to Machine Learning with Python: A Guide for Data Scientists",
    "Vital Introduction to Machine Learning with Python: Best Practices to Improve and Optimize Machine Learning Systems and Algorithms",
    "Machine Learning in Python: Essential Techniques for Predictive Analysis",
    "Python Data Science Handbook: Essential Tools for Working with Data",
    "Introducing Data Science: Big Data, Machine Learning, and more, using Python tools",
    "Real-World Machine Learning"])

labels_one_hot = []
for i in range(len(input_data)):
    labels = np.random.randint(0, 6, max_features)
    labels[labels>1] = 1
    labels_one_hot.append(labels)

labels_one_hot = np.array(labels_one_hot)
 
# Create the text categorical encoding layer.
vectorize_layer = TextVectorization(
         max_tokens=max_features,
         output_mode='int',
         output_sequence_length=max_len)
 
vectorize_layer.adapt(text_dataset)
inp = tf.keras.Input(shape=(1,), dtype=tf.string)
idxs = vectorize_layer(inp)
embed = tf.keras.layers.Embedding(max_features + 1, embedding_dims,input_length=max_len)(idxs)
flat = tf.keras.layers.Flatten()(embed)
out = tf.keras.layers.Dense(labels_one_hot.shape[1])(flat)

model = tf.keras.models.Model(inp, out)

softmax = SampledSoftmaxLoss(model, labels_one_hot.shape[1])

model.compile('adam', loss=softmax.loss)
model.summary()
model.fit(input_data, labels_one_hot)
model.predict(input_data)