# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55707938/typeerror-when-extracting-pincode-from-resume
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import re
    _l_(671769)

except ImportError:
    pass

def pincode_fetch(pincode):
    _l_(671777)

    pincode = _c_(671773, _a_(671771, _n_(671770, "re", lambda: re), "search"), r"^[1-9]\d{5}$", _n_(671772, "pincode", lambda: pincode))
    _l_(671774)
    aux = _n_(671775, "pincode", lambda: pincode)
    _l_(671776)
    return aux

_c_(671782, _n_(671778, "print", lambda: print), _c_(671781, _n_(671779, "pincode_fetch", lambda: pincode_fetch), _n_(671780, "datas", lambda: datas)))
_l_(671783)