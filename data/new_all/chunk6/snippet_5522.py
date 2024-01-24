# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62653214/how-do-i-fix-typeerror-can-only-concatenate-str-not-bytes-to-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
hwa = b'|\x04\x06\r$>'
_l_(345605)

msg = '\xff' * 6 + _n_(345606, "hwa", lambda: hwa) * 16
_l_(345607)
_c_(345610, _n_(345608, "print", lambda: print), _n_(345609, "msg", lambda: msg))
_l_(345611)