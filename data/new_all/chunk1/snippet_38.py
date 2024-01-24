# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/27519306/hashlib-md5-typeerror-unicode-objects-must-be-encoded-before-hashing
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import hashlib
    _l_(398925)

except ImportError:
    pass
a = _c_(398928, _a_(398927, _n_(398926, "hashlib", lambda: hashlib), "md5"))
_l_(398929)
_c_(398932, _a_(398931, _n_(398930, "a", lambda: a), "update"), 'hi')
_l_(398933)
_c_(398936, _a_(398935, _n_(398934, "a", lambda: a), "digest"))
_l_(398937)