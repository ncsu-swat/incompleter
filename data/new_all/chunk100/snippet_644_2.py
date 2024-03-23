# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def count_integer(list1):
    _l_(66314)

    ctr = 0
    _l_(66302)
    for i in _n_(66303, "list1", lambda: list1):
        _l_(66311)

        if _c_(66307, _n_(66304, "isinstance", lambda: isinstance), _n_(66305, "i", lambda: i), _n_(66306, "int", lambda: int)):
            _l_(66310)

            ctr = _n_(66308, "ctr", lambda: ctr) + 1
            _l_(66309)
    aux = _n_(66312, "ctr", lambda: ctr)
    _l_(66313)
    return aux
_c_(66316, _n_(66315, "print", lambda: print), 'Original list:')
_l_(66317)
_c_(66320, _n_(66318, "print", lambda: print), _n_(66319, "list1", lambda: list1))
_l_(66321)
_c_(66323, _n_(66322, "print", lambda: print), '\nNumber of integers in the said mixed list:')
_l_(66324)
_c_(66329, _n_(66325, "print", lambda: print), _c_(66328, _n_(66326, "count_integer", lambda: count_integer), _n_(66327, "list1", lambda: list1)))
_l_(66330)