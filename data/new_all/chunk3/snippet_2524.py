# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73629508/keras-model-fit-typeerror-init-missing-1-required-positional-argument
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(552878)

except ImportError:
    pass
try:
    import sys
    _l_(552880)

except ImportError:
    pass
try:
    import math
    _l_(552882)

except ImportError:
    pass
try:
    import scipy as sp
    _l_(552884)

except ImportError:
    pass
try:
    import tensorflow as tf
    _l_(552886)

except ImportError:
    pass
try:
    from tensorflow.keras.layers import Dense, Flatten
    _l_(552888)

except ImportError:
    pass
try:
    from tensorflow.keras.models import Sequential
    _l_(552890)

except ImportError:
    pass
try:
    from tensorflow.keras.optimizers import Adam
    _l_(552892)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(552894)

except ImportError:
    pass

def get_dataset():
    _l_(552950)

    
    SHOW_IMAGE = False
    _l_(552895)

    mnist = _a_(552899, _a_(552898, _a_(552897, _n_(552896, "tf", lambda: tf), "keras"), "datasets"), "mnist")     # 28x28 images of hand-written digits 0-9
    _l_(552900)     # 28x28 images of hand-written digits 0-9
    (X_train, Y_train), (X_test, Y_test) = _c_(552903, _a_(552902, _n_(552901, "mnist", lambda: mnist), "load_data"))
    _l_(552904)
    
    X_train = _c_(552910, _a_(552908, _a_(552907, _a_(552906, _n_(552905, "tf", lambda: tf), "keras"), "utils"), "normalize"), _n_(552909, "X_train", lambda: X_train),axis=1)  # Normalize input datasets between 0 and 1, Helps the NN converge.
    _l_(552911)  # Normalize input datasets between 0 and 1, Helps the NN converge.
    X_test = _c_(552917, _a_(552915, _a_(552914, _a_(552913, _n_(552912, "tf", lambda: tf), "keras"), "utils"), "normalize"), _n_(552916, "X_test", lambda: X_test),axis=1)
    _l_(552918)

    if _n_(552919, "SHOW_IMAGE", lambda: (SHOW_IMAGE)):
        _l_(552944)

        _c_(552923, _a_(552921, _n_(552920, "plt", lambda: plt), "imshow"), _n_(552922, "X_train", lambda: X_train)[0])
        _l_(552924)
        _c_(552927, _a_(552926, _n_(552925, "plt", lambda: plt), "show"))
        _l_(552928)
        _c_(552930, _n_(552929, "input", lambda: input))
        _l_(552931)
        _c_(552935, _a_(552933, _n_(552932, "plt", lambda: plt), "imshow"), _n_(552934, "Y_train", lambda: Y_train)[0])
        _l_(552936)
        _c_(552939, _a_(552938, _n_(552937, "plt", lambda: plt), "show"))
        _l_(552940)
        _c_(552942, _n_(552941, "input", lambda: input))
        _l_(552943)
    aux = _n_(552945, "X_train", lambda: X_train), _n_(552946, "Y_train", lambda: Y_train), _n_(552947, "X_test", lambda: X_test), _n_(552948, "Y_test", lambda: Y_test)
    _l_(552949)

    return aux

def high_level_neural_net(X_train, Y_train, X_test, Y_test, M, Nnodes1, Nnodes2, inject_layer, af, MAKE_PLOTS):
    _l_(553111)

    
    class InjectInputCallback(_a_(552954, _a_(552953, _a_(552952, _n_(552951, "tf", lambda: tf), "keras"), "callbacks"), "Callback")):
        _l_(552975)


        # Inject input data to layer between residual blocks; I'm unsure if this works yet.

        def __init__(self,train_dataset,layer,logs=None):
            _l_(552961)

            _n_(552955, "self", lambda: self).first_trainds = _n_(552956, "train_dataset", lambda: train_dataset)
            _l_(552957)
            _n_(552958, "self", lambda: self).inject_layer = _n_(552959, "layer", lambda: layer)
            _l_(552960)

        def on_layer_end(self,layer,logs=None):
            _l_(552974)

            _a_(552963, _n_(552962, "model", lambda: model), "layers")[_a_(552965, _n_(552964, "self", lambda: self), "inject_layer")].output = _a_(552970, _a_(552967, _n_(552966, "model", lambda: model), "layers")[_a_(552969, _n_(552968, "self", lambda: self), "inject_layer")], "output") + _a_(552972, _n_(552971, "self", lambda: self), "first_trainds")
            _l_(552973)
    _c_(552977, _n_(552976, "print", lambda: print), '\n')
    _l_(552978)
    
    _c_(552980, _n_(552979, "print", lambda: print), 'Building Sequential Model ...\n')
    _l_(552981)
   
    model = _c_(552983, _n_(552982, "Sequential", lambda: Sequential))
    _l_(552984)
    _c_(552989, _a_(552986, _n_(552985, "model", lambda: model), "add"), _c_(552988, _n_(552987, "Flatten", lambda: Flatten)))
    _l_(552990)
    _c_(552999, _a_(552992, _n_(552991, "model", lambda: model), "add"), _c_(552998, _n_(552993, "Dense", lambda: Dense), _n_(552994, "Nnodes2", lambda: Nnodes2), activation=_a_(552997, _a_(552996, _n_(552995, "tf", lambda: tf), "nn"), "relu")))                                   # Residual block 1 (hidden layers) 
    _l_(553000)                                   # Residual block 1 (hidden layers) 
    _c_(553009, _a_(553002, _n_(553001, "model", lambda: model), "add"), _c_(553008, _n_(553003, "Dense", lambda: Dense), _n_(553004, "Nnodes2", lambda: Nnodes2), activation=_a_(553007, _a_(553006, _n_(553005, "tf", lambda: tf), "nn"), "relu")))                                   # ...
    _l_(553010)                                   # ...
    _c_(553018, _a_(553012, _n_(553011, "model", lambda: model), "add"), _c_(553017, _n_(553013, "Dense", lambda: Dense), 10, activation=_a_(553016, _a_(553015, _n_(553014, "tf", lambda: tf), "nn"), "relu")))                                         # Output layer of residual block 1/Input layer of residual block 2
    _l_(553019)                                         # Output layer of residual block 1/Input layer of residual block 2
    _c_(553028, _a_(553021, _n_(553020, "model", lambda: model), "add"), _c_(553027, _n_(553022, "Dense", lambda: Dense), _n_(553023, "Nnodes2", lambda: Nnodes2), activation=_a_(553026, _a_(553025, _n_(553024, "tf", lambda: tf), "nn"), "relu")))                                   # Residual block 2 (hidden layers)
    _l_(553029)                                   # Residual block 2 (hidden layers)
    _c_(553038, _a_(553031, _n_(553030, "model", lambda: model), "add"), _c_(553037, _n_(553032, "Dense", lambda: Dense), _n_(553033, "Nnodes2", lambda: Nnodes2), activation=_a_(553036, _a_(553035, _n_(553034, "tf", lambda: tf), "nn"), "relu")))                                   # ...
    _l_(553039)                                   # ...
    _c_(553047, _a_(553041, _n_(553040, "model", lambda: model), "add"), _c_(553046, _n_(553042, "Dense", lambda: Dense), 10, activation=_a_(553045, _a_(553044, _n_(553043, "tf", lambda: tf), "nn"), "relu")))                                 # Output layer of residual block 2/Output of neural net 
    _l_(553048)                                 # Output layer of residual block 2/Output of neural net 

    _c_(553050, _n_(553049, "print", lambda: print), 'Compiling ...\n')
    _l_(553051)
    _c_(553056, _a_(553053, _n_(553052, "model", lambda: model), "compile"), optimizer=_c_(553055, _n_(553054, "Adam", lambda: Adam), learning_rate=0.001),  # Uses Adam algorithm as loss function optimizer
                 loss='MeanSquaredError',                                  # sets the model to use MSE as loss function during training
                 metrics=['MeanRelativeError'])                            
    _l_(553057)                            
    
    _c_(553059, _n_(553058, "print", lambda: print), 'Fitting Sequential Model with (X_train, Y_train) ...\n') 
    _l_(553060) 
    
    #tf.print('X_train = ', X_train, 'with shape', tf.shape(X_train), '\n')
    #tf.print('Y_train = ', Y_train, 'with shape', tf.shape(Y_train), '\n')

    _c_(553066, _a_(553062, _n_(553061, "model", lambda: model), "fit"), x=_n_(553063, "X_train", lambda: X_train), y=_n_(553064, "Y_train", lambda: Y_train), epochs=_n_(553065, "M", lambda: M))
    _l_(553067)
    #callbacks=[InjectInputCallback(X_train,inject_layer)]

    if _n_(553068, "MAKE_PLOTS", lambda: (MAKE_PLOTS)):
        _l_(553095)

        _c_(553073, _a_(553070, _n_(553069, "plt", lambda: plt), "plot"), _a_(553072, _n_(553071, "history", lambda: history), "history")['MeanSquareError'])
        _l_(553074)
        _c_(553077, _a_(553076, _n_(553075, "plt", lambda: plt), "title"), 'Model Training')
        _l_(553078)
        _c_(553081, _a_(553080, _n_(553079, "plt", lambda: plt), "ylabel"), 'Mean Squared Error')
        _l_(553082)
        _c_(553085, _a_(553084, _n_(553083, "plt", lambda: plt), "xlabel"), 'Epoch')
        _l_(553086)
        _c_(553089, _a_(553088, _n_(553087, "plt", lambda: plt), "legend"), ['X_Train','Y_Train'], loc='upper right')
        _l_(553090)
        _c_(553093, _a_(553092, _n_(553091, "plt", lambda: plt), "show"))
        _l_(553094)

    #print('Evaluating Sequential Model with Analytic Solution...')
    #model.evaluate()
    
    #print('Predicting')
    #model.predict()

    _c_(553102, _a_(553097, _n_(553096, "model", lambda: model), "build"), _c_(553101, _a_(553099, _n_(553098, "tf", lambda: tf), "shape"), _n_(553100, "X_train", lambda: X_train))) 
    _l_(553103) 
    _c_(553109, _a_(553105, _n_(553104, "tf", lambda: tf), "print"), _c_(553108, _a_(553107, _n_(553106, "model", lambda: model), "summary")))
    _l_(553110)

if (_n_(553112, "__name__", lambda: __name__) == "__main__"):
    _l_(553142)

 
    _c_(553114, _n_(553113, "print", lambda: print), "\n")
    _l_(553115)

    MAKE_PLOTS = True               # Turns on plots during training and evaluation of neural net
    _l_(553116)               # Turns on plots during training and evaluation of neural net

    M = _c_(553120, _n_(553117, "int", lambda: int), _a_(553119, _n_(553118, "sys", lambda: sys), "argv")[1])            # Number of training iterations
    _l_(553121)            # Number of training iterations
   
    Ninputs = 3             # Number of node inputs
    _l_(553122)             # Number of node inputs
    Nnodes1 = 10            # Number of nodes in layers
    _l_(553123)            # Number of nodes in layers
    Nnodes2 = 30            # Number of nodes in 2nd and 4th layers
    _l_(553124)            # Number of nodes in 2nd and 4th layers
    inject_layer = 3        # layer of neural net where we inject input data to output of layer
    _l_(553125)        # layer of neural net where we inject input data to output of layer

    X_train, Y_train, X_test, Y_test = _c_(553127, _n_(553126, "get_dataset", lambda: get_dataset))
    _l_(553128)
    _c_(553140, _n_(553129, "high_level_neural_net", lambda: high_level_neural_net), _n_(553130, "X_train", lambda: X_train), _n_(553131, "Y_train", lambda: Y_train), _n_(553132, "X_test", lambda: X_test), _n_(553133, "Y_test", lambda: Y_test),  _n_(553134, "M", lambda: M), _n_(553135, "Nnodes1", lambda: Nnodes1), _n_(553136, "Nnodes2", lambda: Nnodes2), _n_(553137, "inject_layer", lambda: inject_layer), _n_(553138, "af", lambda: af), _n_(553139, "MAKE_PLOTS", lambda: MAKE_PLOTS))
    _l_(553141)