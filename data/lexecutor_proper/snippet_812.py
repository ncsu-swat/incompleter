# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/15411107/delete-a-dictionary-item-if-the-key-exists
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
keys_to_remove = _c_(65077, _a_(65071, _c_(65070, _n_(65068, "set", lambda: set), _n_(65069, "keys", lambda: keys)), "intersection"), _c_(65076, _n_(65072, "set", lambda: set), _c_(65075, _a_(65074, _n_(65073, "mydict", lambda: mydict), "keys"))))
_l_(65078)
for key in _n_(65079, "keys_to_remove", lambda: keys_to_remove):
    _l_(65081)

    del mydict[key]
    _l_(65080)

keys_to_keep = _c_(65086, _n_(65082, "set", lambda: set), _c_(65085, _a_(65084, _n_(65083, "mydict", lambda: mydict), "keys"))) - _c_(65089, _n_(65087, "set", lambda: set), _n_(65088, "keys", lambda: keys))
_l_(65090)
new_dict = {_n_(65091, "k", lambda: k): _n_(65092, "v", lambda: v) for k, v in _c_(65095, _a_(65094, _n_(65093, "mydict", lambda: mydict), "iteritems")) if _n_(65096, "k", lambda: k) in _n_(65097, "keys_to_keep", lambda: keys_to_keep)}
_l_(65098)

keys_to_keep = _c_(65103, _n_(65099, "set", lambda: set), _c_(65102, _a_(65101, _n_(65100, "mydict", lambda: mydict), "keys"))) - _c_(65106, _n_(65104, "set", lambda: set), _n_(65105, "keys", lambda: keys))
_l_(65107)
new_dict = {_n_(65108, "k", lambda: k): _n_(65109, "mydict", lambda: mydict)[_n_(65110, "k", lambda: k)] for k in _n_(65111, "keys_to_keep", lambda: keys_to_keep)}
_l_(65112)

