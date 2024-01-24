# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62438408/sharing-a-list-between-processes-raises-the-error-attributeerror-forkawareloc
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import multiprocessing
    _l_(560988)

except ImportError:
    pass


def test(c):
    _l_(560991)

    _n_(560989, "c", lambda: c)[0] = 1
    _l_(560990)


class TestClass:
    _l_(561019)

    def __init__(self):
        _l_(561018)

        with _c_(560994, _a_(560993, _n_(560992, "multiprocessing", lambda: multiprocessing), "Manager")) as manager:
            _l_(561013)

            colorcodes = _c_(560997, _a_(560996, _n_(560995, "manager", lambda: manager), "list"))
            _l_(560998)
            p = _c_(561003, _a_(561000, _n_(560999, "multiprocessing", lambda: multiprocessing), "Process"), target=_n_(561001, "test", lambda: test), args=(_n_(561002, "colorcodes", lambda: colorcodes),))
            _l_(561004)
            _c_(561007, _a_(561006, _n_(561005, "p", lambda: p), "start"))
            _l_(561008)
            _c_(561011, _a_(561010, _n_(561009, "p", lambda: p), "join"))
            _l_(561012)
        _c_(561016, _n_(561014, "print", lambda: print), _n_(561015, "colorcodes", lambda: colorcodes)[0])
        _l_(561017)


if _n_(561020, "__name__", lambda: __name__) == '__main__':
    _l_(561024)

    _c_(561022, _n_(561021, "TestClass", lambda: TestClass))
    _l_(561023)