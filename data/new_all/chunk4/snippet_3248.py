# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76734843/attributeerror-module-os-has-no-attribute-killpg
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
if _n_(583699, "__name__", lambda: __name__) == "__main__":
    _l_(583724)

    try:
        _l_(583720)

        _c_(583701, _n_(583700, "main", lambda: main))
        _l_(583702)
    except _n_(583703, "Exception", lambda: Exception):
        _l_(583719)

        exc_info = _c_(583706, _a_(583705, _n_(583704, "sys", lambda: sys), "exc_info"))
        _l_(583707)
        _c_(583711, _a_(583709, _n_(583708, "traceback", lambda: traceback), "print_exception"), *_n_(583710, "exc_info", lambda: exc_info))
        _l_(583712)
        _c_(583717, _a_(583714, _n_(583713, "os", lambda: os), "killpg"), 0, _a_(583716, _n_(583715, "signal", lambda: signal), "SIGKILL"))
        _l_(583718)
    aux = 0
    _l_(583723)

    exit(aux)