# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53426857/typeerror-typedict-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
aFile  = _c_(568811, _n_(568810, "open", lambda: open), "A_FILE.bin", "rb")
_l_(568812)
aBytes = _c_(568815, _a_(568814, _n_(568813, "aFile", lambda: aFile), "read"))
_l_(568816)
cData  = _a_(568823, _c_(568822, _n_(568817, "cast", lambda: cast), _n_(568818, "aBytes", lambda: aBytes), _c_(568821, _n_(568819, "POINTER", lambda: POINTER), _n_(568820, "CData", lambda: CData))), "contents")
_l_(568824)
_c_(568827, _a_(568826, _n_(568825, "aFile", lambda: aFile), "close"))
_l_(568828)