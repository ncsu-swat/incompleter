# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51842008/multiprocessing-attributeerror-imported-object-has-no-attribute-private-m
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from multiprocessing import Process
    _l_(377939)

except ImportError:
    pass
try:
    from ImportedExample import Imported
    _l_(377941)

except ImportError:
    pass

class Example:
    _l_(377948)

    def __init__(self, number):
        _l_(377947)

        _n_(377942, "self", lambda: self).imported = _c_(377945, _n_(377943, "Imported", lambda: Imported), _n_(377944, "number", lambda: number))
        _l_(377946)

def func(example: _n_(377949, "Example", lambda: Example)):
    _l_(377954)

    _c_(377952, _n_(377950, "print", lambda: print), _n_(377951, "example", lambda: example))
    _l_(377953)

if _n_(377955, "__name__", lambda: __name__) == "__main__":
    _l_(377968)

    ex = _c_(377957, _n_(377956, "Example", lambda: Example), 3)
    _l_(377958)

    p = _c_(377962, _n_(377959, "Process", lambda: Process), target=_n_(377960, "func", lambda: func), args=(_n_(377961, "ex", lambda: ex),))
    _l_(377963)
    _c_(377966, _a_(377965, _n_(377964, "p", lambda: p), "start"))
    _l_(377967)