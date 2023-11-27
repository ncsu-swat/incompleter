# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/323972/is-there-any-way-to-kill-a-thread
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from signal import pthread_kill, SIGTSTP
    _l_(1538309)

except ImportError:
    pass
try:
    from threading import Thread
    _l_(1538311)

except ImportError:
    pass
try:
    from itertools import count
    _l_(1538313)

except ImportError:
    pass
try:
    from time import sleep
    _l_(1538315)

except ImportError:
    pass

def target():
    _l_(1538326)

    for num in _c_(1538317, _n_(1538316, "count", lambda: count)):
        _l_(1538325)

        _c_(1538320, _n_(1538318, "print", lambda: print), _n_(1538319, "num", lambda: num))
        _l_(1538321)
        _c_(1538323, _n_(1538322, "sleep", lambda: sleep), 1)
        _l_(1538324)

thread = _c_(1538329, _n_(1538327, "Thread", lambda: Thread), target=_n_(1538328, "target", lambda: target))
_l_(1538330)
_c_(1538333, _a_(1538332, _n_(1538331, "thread", lambda: thread), "start"))
_l_(1538334)
_c_(1538336, _n_(1538335, "sleep", lambda: sleep), 5)
_l_(1538337)
_c_(1538342, _n_(1538338, "pthread_kill", lambda: pthread_kill), _a_(1538340, _n_(1538339, "thread", lambda: thread), "ident"), _n_(1538341, "SIGTSTP", lambda: SIGTSTP))
_l_(1538343)

0
_l_(1538344)
1
_l_(1538345)
2
_l_(1538346)
3
_l_(1538347)
4
_l_(1538348)

[14]+  _n_(1538349, "Stopped", lambda: Stopped)
_l_(1538350)

