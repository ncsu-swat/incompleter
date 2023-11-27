# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/16720541/python-string-replace-regular-expression
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import re
    _l_(1539440)

except ImportError:
    pass
s = "Example String"
_l_(1539441)
replaced = _c_(1539445, _a_(1539443, _n_(1539442, "re", lambda: re), "sub"), '[ES]', 'a', _n_(1539444, "s", lambda: s))
_l_(1539446)
_c_(1539449, _n_(1539447, "print", lambda: print), _n_(1539448, "replaced", lambda: replaced))
_l_(1539450)

