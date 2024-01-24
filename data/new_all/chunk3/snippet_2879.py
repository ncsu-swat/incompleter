# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60120290/building-neural-networks-tensorflow-2-0-model-sub-classing-valueerror-typeer
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tensorflow as tf
    _l_(530733)

except ImportError:
    pass
try:
    from tensorflow.keras import Sequential, Model
    _l_(530735)

except ImportError:
    pass
try:
    from tensorflow.keras.layers import Dense, Input
    _l_(530737)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(530739)

except ImportError:
    pass
try:
    import numpy as np
    _l_(530741)

except ImportError:
    pass


# Read in data-
data = _c_(530744, _a_(530743, _n_(530742, "pd", lambda: pd), "read_csv"), "iris.csv")
_l_(530745)

# Get data types for different attributes-
_a_(530747, _n_(530746, "data", lambda: data), "dtypes")
_l_(530748)
'''
sepallength    float64
sepalwidth     float64
petallength    float64
petalwidth     float64
class           object
dtype: object
'''
_l_(530749)


# Get shape of data-
_a_(530751, _n_(530750, "data", lambda: data), "shape")
_l_(530752)
# (150, 5)


# Check for missing values-
_c_(530758, _a_(530757, _a_(530756, _c_(530755, _a_(530754, _n_(530753, "data", lambda: data), "isnull")), "values"), "any"))
_l_(530759)
# False

# Perform label encoding for target variable-

# Initialize a label encoder-
le = _c_(530761, _n_(530760, "LabelEncoder", lambda: LabelEncoder))
_l_(530762)

# Label encode target attribute-
_n_(530763, "data", lambda: data)['class'] = _c_(530767, _a_(530765, _n_(530764, "le", lambda: le), "fit_transform"), _n_(530766, "data", lambda: data)['class'])
_l_(530768)

# Get different classes which are label encoded-
_a_(530770, _n_(530769, "le", lambda: le), "classes_")
_l_(530771)
# array(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'], dtype=object)

# Split data into features (X) and target (y)-
X = _c_(530774, _a_(530773, _n_(530772, "data", lambda: data), "drop"), 'class', axis = 1)
_l_(530775)
y = _n_(530776, "data", lambda: data)['class']
_l_(530777)


# Get training & testing sets using features and labels-
X_train, X_test, y_train, y_test = _c_(530781, _n_(530778, "train_test_split", lambda: train_test_split), _n_(530779, "X", lambda: X), _n_(530780, "y", lambda: y), test_size=0.3)
_l_(530782)

# Convert from Pandas to numpy arrays-
X_train = _c_(530785, _a_(530784, _n_(530783, "X_train", lambda: X_train), "to_numpy"))
_l_(530786)
X_test = _c_(530789, _a_(530788, _n_(530787, "X_test", lambda: X_test), "to_numpy"))
_l_(530790)

y_train = _c_(530793, _a_(530792, _n_(530791, "y_train", lambda: y_train), "to_numpy"))
_l_(530794)
y_test = _c_(530797, _a_(530796, _n_(530795, "y_test", lambda: y_test), "to_numpy"))
_l_(530798)

_c_(530800, _n_(530799, "print", lambda: print), "\nTraining and Testing set dimensions:")
_l_(530801)
_c_(530809, _n_(530802, "print", lambda: print), _c_(530808, _a_(530803, "X_train.shape = {0}, y_train.shape = {1}", "format"), _a_(530805, _n_(530804, "X_train", lambda: X_train), "shape"), _a_(530807, _n_(530806, "y_train", lambda: y_train), "shape")))
_l_(530810)
_c_(530818, _n_(530811, "print", lambda: print), _c_(530817, _a_(530812, "X_test.shape = {0}, y_test.shape = {1}\n", "format"), _a_(530814, _n_(530813, "X_test", lambda: X_test), "shape"), _a_(530816, _n_(530815, "y_test", lambda: y_test), "shape")))
_l_(530819)
# Training and Testing set dimensions:
# X_train.shape = (105, 4), y_train.shape = (105,)
# X_test.shape = (45, 4), y_test.shape = (45,)



class IrisClassifier(_n_(530820, "Model", lambda: Model)):
    _l_(530876)


    def __init__(self):
        _l_(530854)

        _c_(530825, _a_(530824, _n_(530821, "super", lambda: super)(_n_(530822, "IrisClassifier", lambda: IrisClassifier), _n_(530823, "self", lambda: self)), "__init__"))
        _l_(530826)

        '''
        self.layer1 = Dense(
            units = 4, activation = 'relu',
            kernel_initializer = tf.keras.initializers.GlorotNormal()
            )
        '''
        _l_(530827)

        _n_(530828, "self", lambda: self).input_layer = _c_(530830, _n_(530829, "Input", lambda: Input), shape = (4,)
            )
        _l_(530831)

        _n_(530832, "self", lambda: self).layer1 = _c_(530839, _n_(530833, "Dense", lambda: Dense), units = 10, activation = 'relu',
            input_dim = 4,
            kernel_initializer = _c_(530838, _a_(530837, _a_(530836, _a_(530835, _n_(530834, "tf", lambda: tf), "keras"), "initializers"), "GlorotNormal"))
            )
        _l_(530840)

        _n_(530841, "self", lambda: self).layer2 = _c_(530848, _n_(530842, "Dense", lambda: Dense), units = 10, activation = 'relu',
            kernel_initializer = _c_(530847, _a_(530846, _a_(530845, _a_(530844, _n_(530843, "tf", lambda: tf), "keras"), "initializers"), "GlorotNormal"))
            )
        _l_(530849)

        _n_(530850, "self", lambda: self).outputlayer = _c_(530852, _n_(530851, "Dense", lambda: Dense), units = 3, activation = 'softmax'
            )
        _l_(530853)


    def call(self, x):
        _l_(530875)

        x = _c_(530858, _a_(530856, _n_(530855, "self", lambda: self), "input_layer"), _n_(530857, "x", lambda: x))
        _l_(530859)
        x = _c_(530863, _a_(530861, _n_(530860, "self", lambda: self), "layer1"), _n_(530862, "x", lambda: x))
        _l_(530864)
        x = _c_(530868, _a_(530866, _n_(530865, "self", lambda: self), "layer2"), _n_(530867, "x", lambda: x))
        _l_(530869)
        aux = _c_(530873, _a_(530871, _n_(530870, "self", lambda: self), "outputlayer"), _n_(530872, "x", lambda: x))
        _l_(530874)
        # x = self.layer3(x)

        return aux


# Instantiate a model of defined neural network class-
model = _c_(530878, _n_(530877, "IrisClassifier", lambda: IrisClassifier))
_l_(530879)

# Define EarlyStopping callback-
callback = _c_(530884, _a_(530883, _a_(530882, _a_(530881, _n_(530880, "tf", lambda: tf), "keras"), "callbacks"), "EarlyStopping"), monitor='val_loss', patience=3)
_l_(530885)

# Compile defined model-
_c_(530893, _a_(530887, _n_(530886, "model", lambda: model), "compile"), optimizer=_c_(530892, _a_(530891, _a_(530890, _a_(530889, _n_(530888, "tf", lambda: tf), "keras"), "optimizers"), "Adam"), lr = 0.001),
    loss = 'sparse_categorical_crossentropy',
    metrics = ['accuracy']
     )
_l_(530894)


# Train model-
history2 = _c_(530902, _a_(530896, _n_(530895, "model", lambda: model), "fit"), x = _n_(530897, "X_train", lambda: X_train), y = _n_(530898, "y_train", lambda: y_train),
    validation_data = [_n_(530899, "X_test", lambda: X_test), _n_(530900, "y_test", lambda: y_test)],
    epochs = 50, batch_size = 16,
    callbacks = [_n_(530901, "callback", lambda: callback)]
    )
_l_(530903)