#Source: https://stackoverflow.com/questions/63828775/attributeerror-directoryiterator-object-has-no-attribute-map
datagen = tf.keras.preprocessing.image.ImageDataGenerator(vertical_flip=True)
training_set = datagen.flow_from_directory('/home/train/',target_size=(224, 224), batch_size = 2)

train_dataset = training_set.map(gaussian_filter, num_parallel_calls=tf.data.experimental.AUTOTUNE)