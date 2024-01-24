# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65272979/importing-class-of-module-from-different-path-in-python-nameerror-name-enpy
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(570972)

except ImportError:
    pass
_c_(570976, _a_(570975, _a_(570974, _n_(570973, "sys", lambda: sys), "path"), "insert"), 1, '../enpy')
_l_(570977)
try:
    from enpy import *
    _l_(570979)

except ImportError:
    pass

# TESTING 

# 1. Creating Enpy Object
enpyObj = _c_(570982, _a_(570981, _n_(570980, "enpy", lambda: enpy), "Enpy"), './filetest/train.json')
_l_(570983)