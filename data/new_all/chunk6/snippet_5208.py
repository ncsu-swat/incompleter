# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59915199/error-nameerror-name-json-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from json import *
    _l_(336749)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(336751)

except ImportError:
    pass
try:
    import numpy as np
    _l_(336753)

except ImportError:
    pass
try:
    import os
    _l_(336755)

except ImportError:
    pass

fp=_c_(336757, _n_(336756, "open", lambda: open), "data1.json","r")
_l_(336758)
data=_c_(336762, _a_(336760, _n_(336759, "json", lambda: json), "loads"), _n_(336761, "fp", lambda: fp))
_l_(336763)
_c_(336766, _n_(336764, "print", lambda: print), _n_(336765, "data", lambda: data))
_l_(336767)

s=_c_(336771, _a_(336769, _n_(336768, "pd", lambda: pd), "Series"), _n_(336770, "data", lambda: data),index=[1,2])
_l_(336772)
_c_(336775, _n_(336773, "print", lambda: print), _n_(336774, "s", lambda: s))
_l_(336776)