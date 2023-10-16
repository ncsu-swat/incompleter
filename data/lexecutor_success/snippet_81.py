# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/7370801/how-do-i-measure-elapsed-time-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(1548286)

except ImportError:
    pass

start = _c_(1548289, _a_(1548288, _n_(1548287, "time", lambda: time), "time"))
_l_(1548290)
_c_(1548292, _n_(1548291, "print", lambda: print), "hello")
_l_(1548293)
end = _c_(1548296, _a_(1548295, _n_(1548294, "time", lambda: time), "time"))
_l_(1548297)
_c_(1548301, _n_(1548298, "print", lambda: print), _n_(1548299, "end", lambda: end) - _n_(1548300, "start", lambda: start))
_l_(1548302)

