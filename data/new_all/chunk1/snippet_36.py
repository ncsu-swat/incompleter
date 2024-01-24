# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/20484195/typeerror-range-object-does-not-support-item-assignment
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(414141)

except ImportError:
    pass

emails = {
    "x": "[REDACTED]@hotmail.com",
    "x2": "[REDACTED]@hotmail.com",
    "x3": "[REDACTED]@hotmail.com"
}
_l_(414142)

people = _c_(414145, _a_(414144, _n_(414143, "emails", lambda: emails), "keys"))
_l_(414146)

#generate a number for everyone
allocations = _c_(414151, _n_(414147, "range", lambda: range), _c_(414150, _n_(414148, "len", lambda: len), _n_(414149, "people", lambda: people)))
_l_(414152)
_c_(414156, _a_(414154, _n_(414153, "random", lambda: random), "shuffle"), _n_(414155, "allocations", lambda: allocations))
_l_(414157)