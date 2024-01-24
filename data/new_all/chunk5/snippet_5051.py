# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62877328/typeerror-object-of-type-bool-has-no-len
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
store_id = 1
_l_(663776)
acc_id = _c_(663779, _n_(663777, "str", lambda: str), _n_(663778, "store_id", lambda: store_id))
_l_(663780)
_c_(663785, _n_(663781, "print", lambda: print), "type of acc_id is ", _c_(663784, _n_(663782, "type", lambda: type), _n_(663783, "acc_id", lambda: acc_id)))
_l_(663786)

x = _c_(663789, _n_(663787, "len", lambda: len), _n_(663788, "acc_id", lambda: acc_id))
_l_(663790)
_c_(663793, _n_(663791, "print", lambda: print), _n_(663792, "x", lambda: x))
_l_(663794)

if _c_(663797, _n_(663795, "len", lambda: len), _n_(663796, "acc_id", lambda: acc_id) == 1):
    _l_(663800)

    acc_id += '000' + _n_(663798, "acc_id", lambda: acc_id)
    _l_(663799)