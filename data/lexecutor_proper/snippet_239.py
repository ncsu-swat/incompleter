# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4843173/how-to-check-if-type-of-a-variable-is-string
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import six
    _l_(62121)

except ImportError:
    pass

if _c_(62126, _n_(62122, "isinstance", lambda: isinstance), _n_(62123, "value", lambda: value), _a_(62125, _n_(62124, "six", lambda: six), "string_types")):
    _l_(62128)

    pass # It's a string !!
    _l_(62127) # It's a string !!
try:
    import sys
    _l_(62130)

except ImportError:
    pass

PY3 = _a_(62132, _n_(62131, "sys", lambda: sys), "version_info")[0] == 3
_l_(62133)

if _n_(62134, "PY3", lambda: PY3):
    _l_(62139)

    string_types = _n_(62135, "str", lambda: str),
    _l_(62136)
else:
    string_types = _n_(62137, "basestring", lambda: basestring),
    _l_(62138)

