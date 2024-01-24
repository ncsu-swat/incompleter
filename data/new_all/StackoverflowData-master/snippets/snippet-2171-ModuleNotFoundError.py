#Source: https://stackoverflow.com/questions/59946463/attributeerror-str-object-has-no-attribute-flow-from-directory
import numpy
import numpy as np
from sklearn.linear_model import LogisticRegression
from tensorflow import keras, metrics
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Model
from sklearn.metrics import confusion_matrix
import itertools
import matplotlib.pyplot as plt
from webencodings import labels
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

train_path=r'C:\Users\Acer\imagerec\BAYBAYIN\TRAIN'
valid_path=r'C:\Users\Acer\imagerec\BAYBAYIN\VAL'
test_path=r'C:\Users\Acer\imagerec\BAYBAYIN\TEST'
batch_size=30

class_labels=['A', 'BA', 'KA', 'GA', 'HA', '1', '2', '3', '4', '5', '6', '7',
              '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
              '20', '21', '22', '23', '24', '25', '26', '28', '29', '30', '31', '32',
              '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44']

train_batches=ImageDataGenerator(preprocessing_function=keras.applications.xception.preprocess_input)\
    .flow_from_directory(train_path, target_size=(299,299),classes=class_labels,batch_size=5)
valid_batches=ImageDataGenerator(preprocessing_function=keras.applications.xception.preprocess_input)\
    .flow_from_directory(valid_path, target_size=(299,299),classes=class_labels,batch_size=5)
test_batches=ImageDataGenerator(preprocessing_function=keras.applications.xception.preprocess_input)\
    .flow_from_directory(test_path, target_size=(299,299),classes=class_labels,batch_size=5, shuffle=False)

base_model=keras.applications.vgg19.VGG19(include_top=False)

x=base_model.output
x=GlobalAveragePooling2D()(x)
x=Dense(1024, activation='relu')(x)
x=Dense(48, activation='softmax')(x)
model=Model(inputs=base_model.input, outputs=x)


base_model.trainable = False

N=1

print("HANG ON LEARNING IN PROGRESS...")

model.compile(Adam(lr=.0001),loss='categorical_crossentropy', metrics=['accuracy'])
history=model.fit_generator(train_batches, steps_per_epoch=1290, validation_data=valid_batches,
                            validation_steps=90,epochs=N,verbose=1)

print("[INFO]evaluating model...")

test_labels=test_batches.classes
predictions=model.predict_generator(test_batches, steps=28, verbose=1)


import matplotlib.pyplot as plt
import numpy as np


plt.imshow(np.random.random((48,48)), interpolation='nearest')
plt.xticks(np.arange(0,48), ['A', 'BA', 'KA', 'GA', 'HA', '1', '2', '3', '4', '5', '6', '7',
              '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
              '20', '21', '22', '23', '24', '25', '26', '28', '29', '30', '31', '32',
              '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44'])
plt.yticks(np.arange(0,48),['A', 'BA', 'KA', 'GA', 'HA', '1', '2', '3', '4', '5', '6', '7',
              '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
              '20', '21', '22', '23', '24', '25', '26', '28', '29', '30', '31', '32',
              '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44'])

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

# this is the augmentation configuration we will use for testing:
# only rescaling
test_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_path.flow_from_directory(
    train_path,
    batch_size=batch_size,
    class_mode='categorical')

validation_generator = test_datagen.flow_from_directory(
    valid_path,
    batch_size=batch_size,
    class_mode='categorical')

model.fit_generator(
    train_generator,
    steps_per_epoch= 52800 // batch_size,
    epochs=N,
    validation_data=validation_generator,
    validation_steps= 13200 // batch_size)

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import seaborn as sns


test_steps_per_epoch = numpy.math.ceil(validation_generator.samples / validation_generator.batch_size)

predictions = model.predict_generator(validation_generator, steps=test_steps_per_epoch)
test_steps_per_epoch = numpy.math.ceil(validation_generator.samples / validation_generator.batch_size)
predicted_classes = numpy.argmax(predictions, axis=1)
true_classes = validation_generator.classes
class_labels = list(validation_generator.class_indices.keys())
report = classification_report(true_classes, predicted_classes, target_names=class_labels)
print(report)

cm=confusion_matrix(true_classes,predicted_classes)
print(cm)

plt.show()
model.save("X19baybayin.h5")