# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1305532/how-to-convert-a-nested-python-dict-to-object
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class obj(_n_(62966, "object", lambda: object)):
    _l_(63005)

    def __init__(self, d):
        _l_(63004)

        for k, v in _c_(62969, _a_(62968, _n_(62967, "d", lambda: d), "items")):
            _l_(63003)

            if _c_(62974, _n_(62970, "isinstance", lambda: isinstance), _n_(62971, "k", lambda: k), (_n_(62972, "list", lambda: list), _n_(62973, "tuple", lambda: tuple))):
                _l_(63002)

                _c_(62987, _n_(62975, "setattr", lambda: setattr), _n_(62976, "self", lambda: self), _n_(62977, "k", lambda: k), [_c_(62980, _n_(62978, "obj", lambda: obj), _n_(62979, "x", lambda: x)) if _c_(62984, _n_(62981, "isinstance", lambda: isinstance), _n_(62982, "x", lambda: x), _n_(62983, "dict", lambda: dict)) else _n_(62985, "x", lambda: x) for x in _n_(62986, "v", lambda: v)])
                _l_(62988)
            else:
                _c_(63000, _n_(62989, "setattr", lambda: setattr), _n_(62990, "self", lambda: self), _n_(62991, "k", lambda: k), _c_(62994, _n_(62992, "obj", lambda: obj), _n_(62993, "v", lambda: v)) if _c_(62998, _n_(62995, "isinstance", lambda: isinstance), _n_(62996, "v", lambda: v), _n_(62997, "dict", lambda: dict)) else _n_(62999, "v", lambda: v))
                _l_(63001)

d = {'a': 1, 'b': {'c': 2}, 'd': ["hi", {'foo': "bar"}]}
_l_(63006)
x = _c_(63009, _n_(63007, "obj", lambda: obj), _n_(63008, "d", lambda: d))
_l_(63010)
_a_(63013, _a_(63012, _n_(63011, "x", lambda: x), "b"), "c")
_l_(63014)
2
_l_(63015)
_a_(63018, _a_(63017, _n_(63016, "x", lambda: x), "d")[1], "foo")
_l_(63019)
'bar'
_l_(63020)

