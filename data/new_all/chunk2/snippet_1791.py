# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55582245/subprocess-doesnt-find-my-file-file-not-found-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import subprocess as sb
    _l_(474760)

except ImportError:
    pass
current_path = _c_(474765, _a_(474763, _a_(474762, _n_(474761, "os", lambda: os), "path"), "realpath"), _n_(474764, "__file__", lambda: __file__))
_l_(474766)
_c_(474770, _a_(474768, _n_(474767, "sb", lambda: sb), "call"), ['python3', _n_(474769, "current_path", lambda: current_path)])
_l_(474771)