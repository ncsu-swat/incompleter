# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57595837/attributeerror-module-string-has-no-attribute-capitalize
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import string
    _l_(647007)

except ImportError:
    pass
s = "nishant sharma"
_l_(647008)
str = _c_(647017, _a_(647009, " ", "join"), _c_(647016, _n_(647010, "map", lambda: map), _a_(647012, _n_(647011, "string", lambda: string), "capitalize"), _c_(647015, _a_(647014, _n_(647013, "s", lambda: s), "split"), ' ')))
_l_(647018)
_c_(647021, _n_(647019, "print", lambda: print), _n_(647020, "str", lambda: str))
_l_(647022)