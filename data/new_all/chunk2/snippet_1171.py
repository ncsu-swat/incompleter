# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62632134/python-string-to-array-typeerror-iteration-over-a-0-d-array
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(438136)

except ImportError:
    pass
tags = "[{'thirdParty': 'Funds Transfer'}, {'category': 'External Transfers'}, {'creditDebit': 'credit'}]"
_l_(438137)
# print(type(tags))
# <class 'str'>
arr = _c_(438143, _n_(438138, "list", lambda: list), _c_(438142, _a_(438140, _n_(438139, "np", lambda: np), "array"), _n_(438141, "tags", lambda: tags)))
_l_(438144)
# print(type(tags))
# <class 'numpy.ndarray'>
# print(tags)
# [{'thirdParty': 'Funds Transfer'}, {'category': 'External Transfers'}, {'creditDebit': 'credit'}]
for d in _n_(438145, "arr", lambda: arr):
    _l_(438150)

    _c_(438148, _n_(438146, "print", lambda: print), _n_(438147, "d", lambda: d))
    _l_(438149)