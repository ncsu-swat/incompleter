# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def pairwise(l1):
    _l_(50237)

    temp = []
    _l_(50215)
    for i in _c_(50220, _n_(50216, "range", lambda: range), _c_(50219, _n_(50217, "len", lambda: len), _n_(50218, "l1", lambda: l1)) - 1):
        _l_(50234)

        (current_element, next_element) = (_n_(50221, "l1", lambda: l1)[_n_(50222, "i", lambda: i)], _n_(50223, "l1", lambda: l1)[_n_(50224, "i", lambda: i) + 1])
        _l_(50225)
        x = (_n_(50226, "current_element", lambda: current_element), _n_(50227, "next_element", lambda: next_element))
        _l_(50228)
        _c_(50232, _a_(50230, _n_(50229, "temp", lambda: temp), "append"), _n_(50231, "x", lambda: x))
        _l_(50233)
    aux = _n_(50235, "temp", lambda: temp)
    _l_(50236)
    return aux
_c_(50239, _n_(50238, "print", lambda: print), 'Original lists:')
_l_(50240)
_c_(50243, _n_(50241, "print", lambda: print), _n_(50242, "l1", lambda: l1))
_l_(50244)
_c_(50246, _n_(50245, "print", lambda: print), '\nIterate over all pairs of consecutive items of the said list:')
_l_(50247)
_c_(50252, _n_(50248, "print", lambda: print), _c_(50251, _n_(50249, "pairwise", lambda: pairwise), _n_(50250, "l1", lambda: l1)))
_l_(50253)