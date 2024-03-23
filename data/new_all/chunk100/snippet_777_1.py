# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import re
    _l_(78554)

except ImportError:
    pass
_c_(78556, _n_(78555, "print", lambda: print), 'Original string:')
_l_(78557)
_c_(78560, _n_(78558, "print", lambda: print), _n_(78559, "txt", lambda: txt))
_l_(78561)
new_txt = _c_(78565, _a_(78563, _n_(78562, "re", lambda: re), "sub"), '(?<=\\d)\\s(?=\\d)', '', _n_(78564, "txt", lambda: txt))
_l_(78566)
_c_(78568, _n_(78567, "print", lambda: print), '\nAfter concatenating the consecutive numbers in the said string:')
_l_(78569)
_c_(78572, _n_(78570, "print", lambda: print), _n_(78571, "new_txt", lambda: new_txt))
_l_(78573)