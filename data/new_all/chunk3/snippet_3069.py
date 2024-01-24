# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49932846/typeerror-unsupported-operand-types-for-list-and-int-when-using-dictio
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
alphanumero = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H',
8:'I', 9:'J', 10:'K', 11:'L', 12:'M', 13:'N', 14:'O', 15:'P', 16:'Q',
17:'R', 18:'S', 19:'T', 20:'U', 21:'V', 22:'W', 23:'X', 24:'Y', 25:'Z' }
_l_(576993)

inputlet = _c_(576997, _n_(576994, "str", lambda: str), _c_(576996, _n_(576995, "input", lambda: input), "Enter letter to be encrypted: "))
_l_(576998)
try:
    _l_(577013)

    _c_(577002, _n_(576999, "print", lambda: print), _n_(577000, "alphanumero", lambda: alphanumero)[_n_(577001, "inputlet", lambda: inputlet)])
    _l_(577003)
except _n_(577004, "KeyError", lambda: KeyError):
    _l_(577012)

    letnum = [_n_(577005, "k", lambda: k) for k, v in _c_(577008, _a_(577007, _n_(577006, "alphanumero", lambda: alphanumero), "items")) if _n_(577009, "v", lambda: v) == _n_(577010, "inputlet", lambda: inputlet)[0]]
    _l_(577011)
inputkey = _c_(577017, _n_(577014, "str", lambda: str), _c_(577016, _n_(577015, "input", lambda: input), "Enter key letter: "))
_l_(577018)
try:
    _l_(577033)

    _c_(577022, _n_(577019, "print", lambda: print), _n_(577020, "alphanumero", lambda: alphanumero)[_n_(577021, "inputkey", lambda: inputkey)])
    _l_(577023)
except _n_(577024, "KeyError", lambda: KeyError):
    _l_(577032)

    keynum = [_n_(577025, "u", lambda: u) for u, t in _c_(577028, _a_(577027, _n_(577026, "alphanumero", lambda: alphanumero), "items")) if _n_(577029, "t", lambda: t) == _n_(577030, "inputkey", lambda: inputkey)[0]]
    _l_(577031)
result = (_n_(577034, "letnum", lambda: letnum) + _n_(577035, "keynum", lambda: keynum)) % 26
_l_(577036)
_c_(577039, _n_(577037, "print", lambda: print), _n_(577038, "result", lambda: result))
_l_(577040)