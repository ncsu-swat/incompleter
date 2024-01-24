# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75670256/executing-pandasgui-package-raises-a-attributeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(388429)

except ImportError:
    pass
try:
    from pandasgui import show
    _l_(388431)

except ImportError:
    pass
df = _c_(388434, _a_(388433, _n_(388432, "pd", lambda: pd), "DataFrame"), {'a':[1,2,3], 'b':[4,5,6], 'c':[7,8,9]})
_l_(388435)
_c_(388438, _n_(388436, "show", lambda: show), _n_(388437, "df", lambda: df))
_l_(388439)