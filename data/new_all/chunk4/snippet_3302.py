# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75964010/attributeerror-batchdataset-object-has-no-attribute-class-indices
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class_indices = {}
_l_(601666)
for key in _c_(601670, _a_(601669, _a_(601668, _n_(601667, "train_ds", lambda: train_ds), "class_indices"), "keys")):
    _l_(601677)

    _n_(601671, "class_indices", lambda: class_indices)[_a_(601673, _n_(601672, "train_ds", lambda: train_ds), "class_indices")[_n_(601674, "key", lambda: key)]] = _n_(601675, "key", lambda: key)
    _l_(601676)

_c_(601680, _n_(601678, "print", lambda: print), _n_(601679, "class_indices", lambda: class_indices))
_l_(601681)