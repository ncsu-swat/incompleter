# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54894588/attributeerror-dataframeiterator-object-has-no-attribute-ndim
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(454400)

except ImportError:
    pass
try:
    from keras.models import Sequential
    _l_(454402)

except ImportError:
    pass
try:
    from keras.layers import Convolution2D
    _l_(454404)

except ImportError:
    pass
try:
    from keras.layers import MaxPooling2D
    _l_(454406)

except ImportError:
    pass
try:
    from keras.layers import Flatten
    _l_(454408)

except ImportError:
    pass
try:
    from keras.layers import Dense
    _l_(454410)

except ImportError:
    pass

train = _c_(454413, _a_(454412, _n_(454411, "pd", lambda: pd), "read_csv"), 'train_labels.csv')
_l_(454414)

# Initialising the CNN
classifier = _c_(454416, _n_(454415, "Sequential", lambda: Sequential))
_l_(454417)

# Step 1 - Convolution
_c_(454422, _a_(454419, _n_(454418, "classifier", lambda: classifier), "add"), _c_(454421, _n_(454420, "Convolution2D", lambda: Convolution2D), 32, 3, 3, input_shape = (32, 32, 3), activation = 'relu'))
_l_(454423)

# Step 2 - Pooling
_c_(454428, _a_(454425, _n_(454424, "classifier", lambda: classifier), "add"), _c_(454427, _n_(454426, "MaxPooling2D", lambda: MaxPooling2D), pool_size = (2, 2)))
_l_(454429)

# Adding a second convolutional layer
_c_(454434, _a_(454431, _n_(454430, "classifier", lambda: classifier), "add"), _c_(454433, _n_(454432, "Convolution2D", lambda: Convolution2D), 32, 3, 3, activation = 'relu'))
_l_(454435)
_c_(454440, _a_(454437, _n_(454436, "classifier", lambda: classifier), "add"), _c_(454439, _n_(454438, "MaxPooling2D", lambda: MaxPooling2D), pool_size = (2, 2)))
_l_(454441)

# Step 3 - Flattening
_c_(454446, _a_(454443, _n_(454442, "classifier", lambda: classifier), "add"), _c_(454445, _n_(454444, "Flatten", lambda: Flatten)))
_l_(454447)

# Step 4 - Full connection
_c_(454452, _a_(454449, _n_(454448, "classifier", lambda: classifier), "add"), _c_(454451, _n_(454450, "Dense", lambda: Dense), output_dim = 128, activation = 'relu'))
_l_(454453)
_c_(454458, _a_(454455, _n_(454454, "classifier", lambda: classifier), "add"), _c_(454457, _n_(454456, "Dense", lambda: Dense), output_dim = 1, activation = 'sigmoid'))
_l_(454459)

#add the .tif to the end of the file name
_n_(454460, "train", lambda: train)['id'] = _c_(454464, _a_(454462, _n_(454461, "train", lambda: train)['id'], "astype"), _n_(454463, "str", lambda: str))+'.tif'
_l_(454465)


_c_(454468, _a_(454467, _n_(454466, "classifier", lambda: classifier), "compile"), optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
_l_(454469)
try:
    from keras.preprocessing.image import ImageDataGenerator
    _l_(454471)

except ImportError:
    pass
train_datagen = _c_(454473, _n_(454472, "ImageDataGenerator", lambda: ImageDataGenerator), rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)
_l_(454474)

test_datagen = _c_(454476, _n_(454475, "ImageDataGenerator", lambda: ImageDataGenerator), rescale = 1./255, validation_split = 0.1)
_l_(454477)

training_set = _c_(454481, _a_(454479, _n_(454478, "test_datagen", lambda: test_datagen), "flow_from_dataframe"), dataframe = _n_(454480, "train", lambda: train), 
                                                directory = './train', 
                                                x_col='id', 
                                                y_col='label',
                                                subset = 'training',
                                                target_size=(32, 32), 
                                                batch_size=32, 
                                                shuffle=True,
                                                class_mode = 'binary')
_l_(454482)

test_set = _c_(454486, _a_(454484, _n_(454483, "test_datagen", lambda: test_datagen), "flow_from_dataframe"), dataframe = _n_(454485, "train", lambda: train), 
                                                directory = './train', 
                                                x_col='id', 
                                                y_col='label',
                                                subset = 'validation',
                                                target_size=(32, 32), 
                                                batch_size=32, 
                                                shuffle=True,
                                                class_mode = 'binary')
_l_(454487)




_c_(454492, _a_(454489, _n_(454488, "classifier", lambda: classifier), "fit_generator"), _n_(454490, "training_set", lambda: training_set),
                         steps_per_epoch = 50000,
                         epochs = 25,
                         validation_data=_n_(454491, "test_set", lambda: test_set),
                         validation_steps= 10000)
_l_(454493)
try:
    import matplotlib.pyplot as plt
    _l_(454495)

except ImportError:
    pass
try:
    from sklearn.metrics import roc_curve
    _l_(454497)

except ImportError:
    pass
fpr_keras, tpr_keras, thresholds_keras = _c_(454503, _n_(454498, "roc_curve", lambda: roc_curve), _n_(454499, "classifier", lambda: classifier),
        _c_(454502, _a_(454501, _n_(454500, "predictions", lambda: predictions), "ravel")))
_l_(454504)
try:
    from sklearn.metrics import auc
    _l_(454506)

except ImportError:
    pass
auc_keras = _c_(454510, _n_(454507, "auc", lambda: auc), _n_(454508, "fpr_keras", lambda: fpr_keras), _n_(454509, "tpr_keras", lambda: tpr_keras))
_l_(454511)
_c_(454514, _a_(454513, _n_(454512, "plt", lambda: plt), "plot"), [0, 1], [0, 1], 'k--')
_l_(454515)
_c_(454523, _a_(454517, _n_(454516, "plt", lambda: plt), "plot"), _n_(454518, "fpr_keras", lambda: fpr_keras), _n_(454519, "tpr_keras", lambda: tpr_keras), label=_c_(454522, _a_(454520, 'Keras (area = {:.3f})', "format"), _n_(454521, "auc_keras", lambda: auc_keras)))
_l_(454524)
_c_(454527, _a_(454526, _n_(454525, "plt", lambda: plt), "xlabel"), 'False positive rate')
_l_(454528)
_c_(454531, _a_(454530, _n_(454529, "plt", lambda: plt), "ylabel"), 'True positive rate')
_l_(454532)
_c_(454535, _a_(454534, _n_(454533, "plt", lambda: plt), "title"), 'ROC curve')
_l_(454536)
_c_(454539, _a_(454538, _n_(454537, "plt", lambda: plt), "legend"), loc='best')
_l_(454540)
_c_(454543, _a_(454542, _n_(454541, "plt", lambda: plt), "show"))
_l_(454544)