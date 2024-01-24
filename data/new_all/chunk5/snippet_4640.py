# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53775393/chainer-cnn-typeerror-forward-missing-1-required-positional-argument-x
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from chainer.datasets import split_dataset_random
    _l_(671254)

except ImportError:
    pass
try:
    from chainer.iterators import SerialIterator
    _l_(671256)

except ImportError:
    pass
try:
    from chainer.optimizers import Adam
    _l_(671258)

except ImportError:
    pass
try:
    from chainer.training import Trainer
    _l_(671260)

except ImportError:
    pass
try:
    from chainer.training.updaters import StandardUpdater
    _l_(671262)

except ImportError:
    pass
try:
    from chainer import functions as F, links as L
    _l_(671264)

except ImportError:
    pass
try:
    from chainer import Sequential
    _l_(671266)

except ImportError:
    pass
try:
    import numpy as np
    _l_(671268)

except ImportError:
    pass

batch_size = 3
_l_(671269)

X_train = _c_(671274, _a_(671271, _n_(671270, "np", lambda: np), "ones"), (9957, 60, 80, 3), dtype=_a_(671273, _n_(671272, "np", lambda: np), "float32"))
_l_(671275)
X_train, _ = _c_(671278, _n_(671276, "split_dataset_random", lambda: split_dataset_random), _n_(671277, "X_train", lambda: X_train), 8000, seed=0)
_l_(671279)
train_iter = _c_(671283, _n_(671280, "SerialIterator", lambda: SerialIterator), _n_(671281, "X_train", lambda: X_train), _n_(671282, "batch_size", lambda: batch_size))
_l_(671284)

model = _c_(671304, _n_(671285, "Sequential", lambda: Sequential), _c_(671288, _a_(671287, _n_(671286, "L", lambda: L), "Convolution2D"), None, 64, 3, 2),
    _a_(671290, _n_(671289, "F", lambda: F), "relu"),
    _c_(671293, _a_(671292, _n_(671291, "L", lambda: L), "Convolution2D"), 64, 32, 3, 2),
    _a_(671295, _n_(671294, "F", lambda: F), "relu"),
    _c_(671298, _a_(671297, _n_(671296, "L", lambda: L), "Linear"), None, 16),
    _a_(671300, _n_(671299, "F", lambda: F), "dropout"),
    _c_(671303, _a_(671302, _n_(671301, "L", lambda: L), "Linear"), 16, 4)
)
_l_(671305)

model_loss = _c_(671309, _a_(671307, _n_(671306, "L", lambda: L), "Classifier"), _n_(671308, "model", lambda: model))
_l_(671310)
optimizer = _c_(671312, _n_(671311, "Adam", lambda: Adam))
_l_(671313)
_c_(671317, _a_(671315, _n_(671314, "optimizer", lambda: optimizer), "setup"), _n_(671316, "model_loss", lambda: model_loss))
_l_(671318)
updater = _c_(671322, _n_(671319, "StandardUpdater", lambda: StandardUpdater), _n_(671320, "train_iter", lambda: train_iter), _n_(671321, "optimizer", lambda: optimizer))
_l_(671323)
trainer = _c_(671326, _n_(671324, "Trainer", lambda: Trainer), _n_(671325, "updater", lambda: updater), (25, 'epoch'))
_l_(671327)

_c_(671330, _a_(671329, _n_(671328, "trainer", lambda: trainer), "run"))
_l_(671331)