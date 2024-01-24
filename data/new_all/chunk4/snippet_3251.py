# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76676400/python-thread-typeerror-main-generate-num-argument-after-must-be-an-i
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from threading import Thread, Event
    _l_(624647)

except ImportError:
    pass
try:
    import queue
    _l_(624649)

except ImportError:
    pass
try:
    import random
    _l_(624651)

except ImportError:
    pass

def generate_num(e):
    _l_(624672)

    _c_(624656, _n_(624652, "print", lambda: print), 'e',_c_(624655, _a_(624654, _n_(624653, "e", lambda: e), "is_set")))
    _l_(624657)
    while True:
        _l_(624671)

        if _c_(624660, _a_(624659, _n_(624658, "e", lambda: e), "is_set")):
            _l_(624670)

            _c_(624665, _n_(624661, "print", lambda: print), 'g', _c_(624664, _a_(624663, _n_(624662, "random", lambda: random), "randint"), 15, 20))
            _l_(624666)
        else:
            _c_(624668, _n_(624667, "print", lambda: print), 'g', 0)
            _l_(624669)
def start_generating():
    _l_(624704)

    i = 0
    _l_(624673)
    e = _c_(624675, _n_(624674, "Event", lambda: Event))
    _l_(624676)
    r_thread = _c_(624682, _a_(624681, _c_(624680, _n_(624677, "Thread", lambda: Thread), target=_n_(624678, "generate_num", lambda: generate_num), args=_n_(624679, "e", lambda: (e)), daemon=True), "start"))
    _l_(624683)
    _c_(624685, _n_(624684, "print", lambda: print), 'starting')
    _l_(624686)

    while True:
        _l_(624703)

        _c_(624689, _n_(624687, "print", lambda: print), 'i', _n_(624688, "i", lambda: i))
        _l_(624690)
        if _n_(624691, "i", lambda: i) %5 == 0:
            _l_(624696)

            _c_(624694, _a_(624693, _n_(624692, "e", lambda: e), "set"))
            _l_(624695)
        if _n_(624697, "i", lambda: i) ==12:
            _l_(624701)

            aux = 0
            _l_(624700)
            exit(aux)
        i+=1
        _l_(624702)

_c_(624706, _n_(624705, "start_generating", lambda: start_generating))
_l_(624707)