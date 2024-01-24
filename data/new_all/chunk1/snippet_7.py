# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50997928/typeerror-only-integer-scalar-arrays-can-be-converted-to-a-scalar-index-with-1d
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
bin_probs = [0.5, 0.3, 0.15, 0.04, 0.0025, 0.0025, 0.001, 0.001, 0.001, 0.001, 0.001]
_l_(399850)

X_train = _c_(399854, _n_(399851, "list", lambda: list), _c_(399853, _n_(399852, "range", lambda: range), 2000000))
_l_(399855)

train_probs = _n_(399856, "bin_probs", lambda: bin_probs) * _c_(399864, _n_(399857, "int", lambda: int), _c_(399860, _n_(399858, "len", lambda: len), _n_(399859, "X_train", lambda: X_train)) / _c_(399863, _n_(399861, "len", lambda: len), _n_(399862, "bin_probs", lambda: bin_probs))) # extend probabilities across bin elements
_l_(399865) # extend probabilities across bin elements
_c_(399874, _a_(399867, _n_(399866, "train_probs", lambda: train_probs), "extend"), [0.001]*(_c_(399870, _n_(399868, "len", lambda: len), _n_(399869, "X_train", lambda: X_train)) - _c_(399873, _n_(399871, "len", lambda: len), _n_(399872, "train_probs", lambda: train_probs)))) # a small fix to match number of elements
_l_(399875) # a small fix to match number of elements
train_probs = _n_(399876, "train_probs", lambda: train_probs)/_c_(399880, _a_(399878, _n_(399877, "np", lambda: np), "sum"), _n_(399879, "train_probs", lambda: train_probs)) # normalize
_l_(399881) # normalize
indices = _c_(399891, _a_(399884, _a_(399883, _n_(399882, "np", lambda: np), "random"), "choice"), _c_(399889, _n_(399885, "range", lambda: range), _c_(399888, _n_(399886, "len", lambda: len), _n_(399887, "X_train", lambda: X_train))), replace=False, size=50000, p=_n_(399890, "train_probs", lambda: train_probs))
_l_(399892)
out_images = _n_(399893, "X_train", lambda: X_train)[_c_(399897, _a_(399895, _n_(399894, "indices", lambda: indices), "astype"), _n_(399896, "int", lambda: int))] # this is where I get the error
_l_(399898) # this is where I get the error