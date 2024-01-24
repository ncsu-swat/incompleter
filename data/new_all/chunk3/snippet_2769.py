# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63841876/typeerror-list-object-is-not-an-iterator-tensorflow-custom-metric-callback
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn.datasets import load_breast_cancer
    _l_(569372)

except ImportError:
    pass
try:
    from sklearn.model_selection import train_test_split
    _l_(569374)

except ImportError:
    pass
try:
    from sklearn.metrics import precision_score, recall_score, f1_score
    _l_(569376)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(569378)

except ImportError:
    pass
try:
    import numpy as np
    _l_(569380)

except ImportError:
    pass
try:
    from tensorflow.keras.models import Sequential
    _l_(569382)

except ImportError:
    pass
try:
    from tensorflow.keras.layers import Dense
    _l_(569384)

except ImportError:
    pass
try:
    from tensorflow.keras.optimizers import Adam
    _l_(569386)

except ImportError:
    pass
try:
    from tensorflow.keras.callbacks import Callback
    _l_(569388)

except ImportError:
    pass

# Get binary classification dataset
data = _c_(569390, _n_(569389, "load_breast_cancer", lambda: load_breast_cancer), as_frame=True)
_l_(569391)
_c_(569394, _n_(569392, "print", lambda: print), _n_(569393, "data", lambda: data))
_l_(569395)
df = _n_(569396, "data", lambda: data)['data']
_l_(569397)
_n_(569398, "df", lambda: df)['target'] = _n_(569399, "data", lambda: data)['target']
_l_(569400)

# Train Test split
train, test = _c_(569403, _n_(569401, "train_test_split", lambda: train_test_split), _n_(569402, "data", lambda: data), test_size = 0.10, shuffle=False)
_l_(569404)

# Define features and labels
x_train = _a_(569406, _n_(569405, "train", lambda: train), "iloc")[:, :-1]
_l_(569407)
y_train = _a_(569409, _n_(569408, "train", lambda: train), "iloc")[:, -1]
_l_(569410)
x_test = _a_(569412, _n_(569411, "test", lambda: test), "iloc")[:, :-1]
_l_(569413)
y_test = _a_(569415, _n_(569414, "test", lambda: test), "iloc")[:, -1]
_l_(569416)

# https://github.com/keras-team/keras/issues/10472#issuecomment-472543538
class Metrics(_n_(569417, "Callback", lambda: Callback)):
    _l_(569531)

    
    def __init__(self, val_data, batch_size=20):
        _l_(569428)

        _c_(569420, _a_(569419, _n_(569418, "super", lambda: super)(), "__init__"))
        _l_(569421)
        _n_(569422, "self", lambda: self).validation_data = _n_(569423, "val_data", lambda: val_data)
        _l_(569424)
        _n_(569425, "self", lambda: self).batch_size = _n_(569426, "batch_size", lambda: batch_size)
        _l_(569427)
    
    def on_train_begin(self, logs={}):
        _l_(569435)

        # print(self.validation_data)
        _n_(569429, "self", lambda: self).val_f1s = []
        _l_(569430)
        _n_(569431, "self", lambda: self).val_recalls = []
        _l_(569432)
        _n_(569433, "self", lambda: self).val_precisions = []
        _l_(569434)
    def on_epoch_end(self, epoch, logs={}):
        _l_(569530)

        batches = _c_(569439, _n_(569436, "len", lambda: len), _a_(569438, _n_(569437, "self", lambda: self), "validation_data"))
        _l_(569440)
        total = _n_(569441, "batches", lambda: batches) * _a_(569443, _n_(569442, "self", lambda: self), "batch_size")
        _l_(569444)
        
        val_pred = _c_(569448, _a_(569446, _n_(569445, "np", lambda: np), "zeros"), (_n_(569447, "total", lambda: total),1))
        _l_(569449)
        val_true = _c_(569453, _a_(569451, _n_(569450, "np", lambda: np), "zeros"), _n_(569452, "total", lambda: (total)))
        _l_(569454)
        
        for batch in _c_(569457, _n_(569455, "range", lambda: range), _n_(569456, "batches", lambda: batches)):
            _l_(569490)

            xVal, yVal = _c_(569461, _n_(569458, "next", lambda: next), _a_(569460, _n_(569459, "self", lambda: self), "validation_data"))
            _l_(569462)
            _n_(569463, "val_pred", lambda: val_pred)[_n_(569464, "batch", lambda: batch) * _a_(569466, _n_(569465, "self", lambda: self), "batch_size") : (_n_(569467, "batch", lambda: batch)+1) * _a_(569469, _n_(569468, "self", lambda: self), "batch_size")] = _c_(569479, _a_(569478, _c_(569477, _a_(569471, _n_(569470, "np", lambda: np), "asarray"), _c_(569476, _a_(569474, _a_(569473, _n_(569472, "self", lambda: self), "model"), "predict"), _n_(569475, "xVal", lambda: xVal))), "round"))
            _l_(569480)
            _n_(569481, "val_true", lambda: val_true)[_n_(569482, "batch", lambda: batch) * _a_(569484, _n_(569483, "self", lambda: self), "batch_size") : (_n_(569485, "batch", lambda: batch)+1) * _a_(569487, _n_(569486, "self", lambda: self), "batch_size")] = _n_(569488, "yVal", lambda: yVal)
            _l_(569489)
        val_pred = _c_(569494, _a_(569492, _n_(569491, "np", lambda: np), "squeeze"), _n_(569493, "val_pred", lambda: val_pred))
        _l_(569495)
        _val_f1 = _c_(569499, _n_(569496, "f1_score", lambda: f1_score), _n_(569497, "val_true", lambda: val_true), _n_(569498, "val_pred", lambda: val_pred))
        _l_(569500)
        _val_precision = _c_(569504, _n_(569501, "precision_score", lambda: precision_score), _n_(569502, "val_true", lambda: val_true), _n_(569503, "val_pred", lambda: val_pred))
        _l_(569505)
        _val_recall = _c_(569509, _n_(569506, "recall_score", lambda: recall_score), _n_(569507, "val_true", lambda: val_true), _n_(569508, "val_pred", lambda: val_pred))
        _l_(569510)
        
        _c_(569515, _a_(569513, _a_(569512, _n_(569511, "self", lambda: self), "val_f1s"), "append"), _n_(569514, "_val_f1", lambda: _val_f1))
        _l_(569516)
        _c_(569521, _a_(569519, _a_(569518, _n_(569517, "self", lambda: self), "val_recalls"), "append"), _n_(569520, "_val_recall", lambda: _val_recall))
        _l_(569522)
        _c_(569527, _a_(569525, _a_(569524, _n_(569523, "self", lambda: self), "val_precisions"), "append"), _n_(569526, "_val_precision", lambda: _val_precision))
        _l_(569528)
        aux = ""
        _l_(569529)
        
        return aux

# Define a function that creates a basic model
def make_deep_learning_classifier():
    _l_(569565)

    model = _c_(569533, _n_(569532, "Sequential", lambda: Sequential))
    _l_(569534)
    _c_(569541, _a_(569536, _n_(569535, "model", lambda: model), "add"), _c_(569540, _n_(569537, "Dense", lambda: Dense), 64, activation='relu', input_dim=_a_(569539, _n_(569538, "x_train", lambda: x_train), "shape")[1], kernel_initializer='normal'))
    _l_(569542)
    _c_(569549, _a_(569544, _n_(569543, "model", lambda: model), "add"), _c_(569548, _n_(569545, "Dense", lambda: Dense), 32, activation='relu', input_dim=_a_(569547, _n_(569546, "x_train", lambda: x_train), "shape")[1], kernel_initializer='normal'))
    _l_(569550)
    _c_(569555, _a_(569552, _n_(569551, "model", lambda: model), "add"), _c_(569554, _n_(569553, "Dense", lambda: Dense), 1, kernel_initializer='normal', activation='sigmoid'))
    _l_(569556)
    _c_(569561, _a_(569558, _n_(569557, "model", lambda: model), "compile"), loss='binary_crossentropy', optimizer=_c_(569560, _n_(569559, "Adam", lambda: Adam)), metrics=['accuracy'])
    _l_(569562)
    aux = _n_(569563, "model", lambda: model)
    _l_(569564)
    return aux

# Get our model
model = _c_(569567, _n_(569566, "make_deep_learning_classifier", lambda: make_deep_learning_classifier))
_l_(569568)
_c_(569573, _n_(569569, "print", lambda: print), _c_(569572, _a_(569571, _n_(569570, "model", lambda: model), "summary")))
_l_(569574)

# Define some params
batch_size = 32
_l_(569575)

# Call our custom callback
callback = [_c_(569580, _n_(569576, "Metrics", lambda: Metrics), val_data=[_n_(569577, "x_test", lambda: x_test), _n_(569578, "y_test", lambda: y_test)], batch_size=_n_(569579, "batch_size", lambda: batch_size))] # < Issue here?
_l_(569581) # < Issue here?

# Start training
_c_(569590, _a_(569583, _n_(569582, "model", lambda: model), "fit"), _n_(569584, "x_train", lambda: x_train), _n_(569585, "y_train", lambda: y_train), epochs=1000, batch_size=_n_(569586, "batch_size", lambda: batch_size), verbose=1, callbacks=_n_(569587, "callback", lambda: callback), validation_data=(_n_(569588, "x_test", lambda: x_test), _n_(569589, "y_test", lambda: y_test)))
_l_(569591)
_c_(569595, _n_(569592, "print", lambda: print), _a_(569594, _n_(569593, "Metrics", lambda: Metrics), "val_precisions")) # < Issue here?
_l_(569596) # < Issue here?