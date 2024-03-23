# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def relative_order(lst):
    _l_(38665)

    result = [_n_(38654, "i", lambda: i) for i in _c_(38659, _n_(38655, "range", lambda: range), _c_(38658, _n_(38656, "len", lambda: len), _n_(38657, "lst", lambda: lst))) if _n_(38660, "lst", lambda: lst)[_n_(38661, "i", lambda: i)] == None]
    _l_(38662)
    aux = _n_(38663, "result", lambda: result)
    _l_(38664)
    return aux
_c_(38667, _n_(38666, "print", lambda: print), 'Original list:')
_l_(38668)
_c_(38671, _n_(38669, "print", lambda: print), _n_(38670, "nums", lambda: nums))
_l_(38672)
_c_(38674, _n_(38673, "print", lambda: print), '\nIndexes of all None items of the list:')
_l_(38675)
_c_(38680, _n_(38676, "print", lambda: print), _c_(38679, _n_(38677, "relative_order", lambda: relative_order), _n_(38678, "nums", lambda: nums)))
_l_(38681)