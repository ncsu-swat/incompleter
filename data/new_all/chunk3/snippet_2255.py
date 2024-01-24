# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55559561/nameerror-name-model-is-not-defined-in-python-code-for-isolated-speech-recogn
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn.model_selection import StratifiedShuffleSplit
    _l_(578895)

except ImportError:
    pass
sss = _c_(578897, _n_(578896, "StratifiedShuffleSplit", lambda: StratifiedShuffleSplit), test_size=0.1, random_state=0)
_l_(578898)

for n,i in _c_(578901, _n_(578899, "enumerate", lambda: enumerate), _n_(578900, "all_obs", lambda: all_obs)):
    _l_(578909)

    _n_(578902, "all_obs", lambda: all_obs)[_n_(578903, "n", lambda: n)] /= _c_(578907, _a_(578906, _n_(578904, "all_obs", lambda: all_obs)[_n_(578905, "n", lambda: n)], "sum"), axis=0)
    _l_(578908)


for train_index, test_index in _c_(578914, _a_(578911, _n_(578910, "sss", lambda: sss), "split"), _n_(578912, "all_obs", lambda: all_obs), _n_(578913, "all_labels", lambda: all_labels)):
    _l_(578925)

    X_train, X_test = _n_(578915, "all_obs", lambda: all_obs)[_n_(578916, "train_index", lambda: train_index), ...], _n_(578917, "all_obs", lambda: all_obs)[_n_(578918, "test_index", lambda: test_index), ...]
    _l_(578919)
    y_train, y_test = _n_(578920, "all_labels", lambda: all_labels)[_n_(578921, "train_index", lambda: train_index)], _n_(578922, "all_labels", lambda: all_labels)[_n_(578923, "test_index", lambda: test_index)]
    _l_(578924)
ys = _c_(578928, _n_(578926, "set", lambda: set), _n_(578927, "all_labels", lambda: all_labels))
_l_(578929)
ms = [_c_(578931, _n_(578930, "gmmhmm", lambda: gmmhmm), 7) for y in _n_(578932, "ys", lambda: ys)]
_l_(578933)

_ = [_c_(578939, _a_(578935, _n_(578934, "model", lambda: model), "train"), _n_(578936, "X_train", lambda: X_train)[_n_(578937, "y_train", lambda: y_train) == _n_(578938, "y", lambda: y), :, :]) for m, y in _c_(578943, _n_(578940, "zip", lambda: zip), _n_(578941, "ms", lambda: ms), _n_(578942, "ys", lambda: ys))]
_l_(578944)
ps1 = [_c_(578948, _a_(578946, _n_(578945, "model", lambda: model), "test"), _n_(578947, "X_test", lambda: X_test)) for m in _n_(578949, "ms", lambda: ms)]
_l_(578950)
res1 = _c_(578954, _a_(578952, _n_(578951, "np", lambda: np), "vstack"), _n_(578953, "ps1", lambda: ps1))
_l_(578955)
predicted_label1 = _c_(578959, _a_(578957, _n_(578956, "np", lambda: np), "argmax"), _n_(578958, "res1", lambda: res1), axis=0)
_l_(578960)
dictionary = ['apple', 'banana', 'elephant', 'dog', 'frog', 'cat', 'jack', 'god', 'Intelligent', 'hello']
_l_(578961)
spoken_word = []
_l_(578962)
for i in _n_(578963, "predicted_label1", lambda: predicted_label1):
    _l_(578970)

    _c_(578968, _a_(578965, _n_(578964, "spoken_word", lambda: spoken_word), "append"), _n_(578966, "dictionary", lambda: dictionary)[_n_(578967, "i", lambda: i)])
    _l_(578969)
_c_(578973, _n_(578971, "print", lambda: print), _n_(578972, "spoken_word", lambda: spoken_word))
_l_(578974)
missed = (_n_(578975, "predicted_label1", lambda: predicted_label1) != _n_(578976, "y_test", lambda: y_test))
_l_(578977)
_c_(578983, _n_(578978, "print", lambda: print), 'Test accuracy: %.2f percent' % (100 * (1 - _c_(578982, _a_(578980, _n_(578979, "np", lambda: np), "mean"), _n_(578981, "missed", lambda: missed)))))
_l_(578984)