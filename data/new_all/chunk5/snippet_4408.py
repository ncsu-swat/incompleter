# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58168843/typeerror-init-missing-1-required-positional-argument-kernel-size
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def fish_model():
    _l_(649000)

    model = _c_(648943, _n_(648942, "Sequential", lambda: Sequential))
    _l_(648944)
    try:
        from keras.layers import Activation, Dense
        _l_(648946)

    except ImportError:
        pass
    try:
        from keras.layers.convolutional import Convolution2D
        _l_(648948)

    except ImportError:
        pass
    try:
        from keras.layers.convolutional import MaxPooling2D
        _l_(648950)

    except ImportError:
        pass
    try:
        from keras.layers import Dropout
        _l_(648952)

    except ImportError:
        pass
    _c_(648957, _a_(648954, _n_(648953, "model", lambda: model), "add"), _c_(648956, _n_(648955, "Convolution2D", lambda: Convolution2D), filters=(6,3,3),input_shape=(256,768,1),activation='relu'))
    _l_(648958)
    _c_(648963, _a_(648960, _n_(648959, "model", lambda: model), "add"), _c_(648962, _n_(648961, "MaxPooling2D", lambda: MaxPooling2D), pool_size=(2,2),strides=2))
    _l_(648964)
    _c_(648969, _a_(648966, _n_(648965, "model", lambda: model), "add"), _c_(648968, _n_(648967, "Convolution2D", lambda: Convolution2D), filters=6, nb_row=3, nb_col=3,subsample=(2,2),
    input_shape=(256, 768, 1,), activation='relu', border_mode='same'))
    _l_(648970)
    _c_(648975, _a_(648972, _n_(648971, "model", lambda: model), "add"), _c_(648974, _n_(648973, "Dropout", lambda: Dropout), 0.1))
    _l_(648976)
    _c_(648981, _a_(648978, _n_(648977, "model", lambda: model), "add"), _c_(648980, _n_(648979, "Flatten", lambda: Flatten)))
    _l_(648982)
    _c_(648987, _a_(648984, _n_(648983, "model", lambda: model), "add"), _c_(648986, _n_(648985, "Dense", lambda: Dense), 8, activation='softmax'))
    _l_(648988)
    epochs = 5
    _l_(648989)
    lrate = 0.1
    _l_(648990)
    decay = _n_(648991, "lrate", lambda: lrate)/_n_(648992, "epochs", lambda: epochs)
    _l_(648993)
    #sgd = SGD(lr=lrate, momentum=0.5, decay=decay, nesterov=False)
    _c_(648996, _a_(648995, _n_(648994, "model", lambda: model), "compile"), loss='categorical_crossentropy', optimizer='sgd', metrics=['categorical_accuracy'])
    _l_(648997)
    aux = _n_(648998, "model", lambda: model)
    _l_(648999)
    return aux

model= _c_(649002, _n_(649001, "fish_model", lambda: fish_model))
_l_(649003)
_c_(649008, _n_(649004, "print", lambda: print), _c_(649007, _a_(649006, _n_(649005, "model", lambda: model), "summary")))
_l_(649009)
history = _c_(649016, _a_(649011, _n_(649010, "model", lambda: model), "fit"), _n_(649012, "X_train", lambda: X_train), _n_(649013, "Y_train", lambda: Y_train), validation_data=(_n_(649014, "x_validation", lambda: x_validation), _n_(649015, "y_validation", lambda: y_validation)), nb_epoch=6, batch_size=4)
_l_(649017)