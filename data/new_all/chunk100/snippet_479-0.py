# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def pairwise(l1):
    _l_(118025)

    temp = []
    _l_(118003)
    for i in _c_(118008, _n_(118004, "range", lambda: range), _c_(118007, _n_(118005, "len", lambda: len), _n_(118006, "l1", lambda: l1)) - 1):
        _l_(118022)

        current_element, next_element = (_n_(118009, "l1", lambda: l1)[_n_(118010, "i", lambda: i)], _n_(118011, "l1", lambda: l1)[_n_(118012, "i", lambda: i) + 1])
        _l_(118013)
        x = (_n_(118014, "current_element", lambda: current_element), _n_(118015, "next_element", lambda: next_element))
        _l_(118016)
        _c_(118020, _a_(118018, _n_(118017, "temp", lambda: temp), "append"), _n_(118019, "x", lambda: x))
        _l_(118021)
    aux = _n_(118023, "temp", lambda: temp)
    _l_(118024)
    return aux
_c_(118027, _n_(118026, "print", lambda: print), 'Original lists:')
_l_(118028)
_c_(118031, _n_(118029, "print", lambda: print), _n_(118030, "l1", lambda: l1))
_l_(118032)
_c_(118034, _n_(118033, "print", lambda: print), '\nIterate over all pairs of consecutive items of the said list:')
_l_(118035)
_c_(118040, _n_(118036, "print", lambda: print), _c_(118039, _n_(118037, "pairwise", lambda: pairwise), _n_(118038, "l1", lambda: l1)))
_l_(118041)