# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70657867/nameerror-name-encode-is-not-defined-while-trying-to-format-an-object-to-j
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import json
    _l_(589863)

except ImportError:
    pass

class person:
    _l_(589871)

    def __init__(self, name, age):
        _l_(589870)

        _n_(589864, "self", lambda: self).name = _n_(589865, "name", lambda: name)
        _l_(589866)
        _n_(589867, "self", lambda: self).age = _n_(589868, "age", lambda: age)
        _l_(589869)


bob = _c_(589873, _n_(589872, "person", lambda: person), "Bob", 5)
_l_(589874)


class encode_Obj:
    _l_(589889)


    def encode(x):
        _l_(589888)

        if _c_(589878, _n_(589875, "isinstance", lambda: isinstance), _n_(589876, "x", lambda: x), _n_(589877, "person", lambda: person)):
            _l_(589887)

            aux = {"name": _a_(589880, _n_(589879, "x", lambda: x), "name"), "age": _a_(589882, _n_(589881, "x", lambda: x), "age")}
            _l_(589883)
            return aux
        else:
            raise _c_(589885, _n_(589884, "TypeError", lambda: TypeError), "Object of type user is not JSON serializable")
            _l_(589886)


bob_JSON = _c_(589894, _a_(589891, _n_(589890, "json", lambda: json), "dumps"), _n_(589892, "bob", lambda: bob), default=_n_(589893, "encode", lambda: encode))
_l_(589895)
_c_(589898, _n_(589896, "print", lambda: print), _n_(589897, "bob_JSON", lambda: bob_JSON))
_l_(589899)