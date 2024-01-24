# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46781937/missing-arguments-and-type-errors
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def bs(L, item, left, right):
    _l_(618878)

    if _n_(618840, "right", lambda: right) is None:
        _l_(618845)

        right = _c_(618843, _n_(618841, "len", lambda: len), _n_(618842, "L", lambda: L))
        _l_(618844)
    if _n_(618846, "right", lambda: right) - _n_(618847, "left", lambda: left) == 0:
        _l_(618849)

        aux = False
        _l_(618848)
        return aux
    if _n_(618850, "right", lambda: right) - _n_(618851, "left", lambda: left) == 1:
        _l_(618856)

        aux = _n_(618852, "L", lambda: L)[_n_(618853, "left", lambda: left)] == _n_(618854, "item", lambda: item)
        _l_(618855)
        return aux
    median = (_n_(618857, "right", lambda: right) + _n_(618858, "left", lambda: left))//2
    _l_(618859)
    if _n_(618860, "item", lambda: item) < _n_(618861, "L", lambda: L)[_n_(618862, "median", lambda: median)]:
        _l_(618877)

        aux = _c_(618868, _n_(618863, "bs", lambda: bs), _n_(618864, "L", lambda: L), _n_(618865, "item", lambda: item), _n_(618866, "left", lambda: left), _n_(618867, "median", lambda: median))
        _l_(618869)
        return aux
    else:
        aux = _c_(618875, _n_(618870, "bs", lambda: bs), _n_(618871, "L", lambda: L), _n_(618872, "item", lambda: item), _n_(618873, "median", lambda: median), _n_(618874, "right", lambda: right))
        _l_(618876)
        return aux

L = [_n_(618879, "i", lambda: i) for i in _c_(618881, _n_(618880, "range", lambda: range), 10)]
_l_(618882)
for i in _c_(618884, _n_(618883, "range", lambda: range), 20):
    _l_(618892)

    _c_(618890, _n_(618885, "print", lambda: print), _c_(618889, _n_(618886, "bs", lambda: bs), _n_(618887, "L", lambda: L), _n_(618888, "i", lambda: i)))
    _l_(618891)