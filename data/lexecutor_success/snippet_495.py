# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3389574/check-if-multiple-strings-exist-in-another-string
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
a = ['a', 'b', 'c']
_l_(1541747)
str = "a123"
_l_(1541748)
if _c_(1541751, _n_(1541749, "set", lambda: set), _n_(1541750, "a", lambda: a)) & _c_(1541754, _n_(1541752, "set", lambda: set), _n_(1541753, "str", lambda: str)):
    _l_(1541761)

    _c_(1541756, _n_(1541755, "print", lambda: print), "some of the strings found in str")
    _l_(1541757)
else:
    _c_(1541759, _n_(1541758, "print", lambda: print), "no strings found in str")
    _l_(1541760)

