# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/295135/turn-a-string-into-a-valid-filename
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import re
    _l_(1538511)

except ImportError:
    pass
t = _c_(1538514, _a_(1538513, _n_(1538512, "re", lambda: re), "compile"), "[a-zA-Z0-9.,_-]")
_l_(1538515)
unsafe = "abc∂éåß®∆˚˙©¬ñ√ƒµ©∆∫ø"
_l_(1538516)
safe = [_n_(1538517, "ch", lambda: ch) for ch in _n_(1538518, "unsafe", lambda: unsafe) if _c_(1538522, _a_(1538520, _n_(1538519, "t", lambda: t), "match"), _n_(1538521, "ch", lambda: ch))]
_l_(1538523)
try:
    from random import choice
    _l_(1538525)

except ImportError:
    pass
try:
    from string import ascii_lowercase, ascii_uppercase, digits
    _l_(1538527)

except ImportError:
    pass
allowed_chr = _n_(1538528, "ascii_lowercase", lambda: ascii_lowercase) + _n_(1538529, "ascii_uppercase", lambda: ascii_uppercase) + _n_(1538530, "digits", lambda: digits)
_l_(1538531)

safe = _c_(1538538, _a_(1538532, '', "join"), [_c_(1538535, _n_(1538533, "choice", lambda: choice), _n_(1538534, "allowed_chr", lambda: allowed_chr)) for _ in _c_(1538537, _n_(1538536, "range", lambda: range), 16)])
_l_(1538539)
# => 'CYQ4JDKE9JfcRzAZ'

