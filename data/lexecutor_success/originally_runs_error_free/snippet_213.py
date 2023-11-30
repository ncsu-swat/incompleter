# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5971312/how-to-set-environment-variables-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(1539627)

except ImportError:
    pass

if not _c_(1539631, _a_(1539630, _a_(1539629, _n_(1539628, "os", lambda: os), "environ"), "get"), "DEBUSSY"):
    _l_(1539640)

    _c_(1539635, _a_(1539634, _a_(1539633, _n_(1539632, "os", lambda: os), "environ"), "setdefault"), "DEBUSSY","1")
    _l_(1539636)
else:
     _a_(1539638, _n_(1539637, "os", lambda: os), "environ")["DEBUSSY"] = "1"
     _l_(1539639)

_c_(1539644, _n_(1539641, "print", lambda: print), _a_(1539643, _n_(1539642, "os", lambda: os), "environ")["DEBUSSY"])
_l_(1539645)


